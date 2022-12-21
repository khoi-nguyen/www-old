ACTIVATE := .venv/bin/activate
ENV := . $(ACTIVATE);
ifeq (${ENVIRONMENT},production)
	ACTIVATE :=
	ENV :=
endif
PYTHON := $(ENV) python
FIND := find ./ -not -path "*/.*" -not -path "*/julia/*" -type f -name

META := $(shell $(FIND) '*.yaml')
MARKDOWN := $(shell $(FIND) '*.md')
JSON := $(addprefix build/, $(MARKDOWN:.md=.json))
PAGES := $(addprefix build/, $(MARKDOWN:.md=.html))

.PHONY: all backend clean watch

all: $(JSON) $(PAGES) static/highlight.css 

backend: $(ACTIVATE) $(JSON) $(PAGES)
	@$(PYTHON) -m app

.venv/bin/activate: requirements.txt
	@test -d .venv || python -m venv .venv
	@$(PYTHON) -m pip install -Ur requirements.txt
	@touch .venv/bin/activate

build/%.json: %.md Makefile bin/ $(META)
	@echo "Building $@"
	@mkdir -p $(@D)
	@./bin/convert $< --template="templates/json.html" > $@

build/%.html: %.md build/%.json Makefile bin/ bin/filters $(META) $(ACTIVATE)
	@echo "Building $@"
	@mkdir -p $(@D)
	@$(ENV) ./bin/convert $< --citeproc --mathjax \
		--email-obfuscation=javascript \
		--filter bin/filters/bootstrap.py \
		--filter bin/filters/environments.py \
		--filter bin/filters/mermaid.py \
		--filter bin/filters/slideshow.py \
		--filter bin/filters/plots.py \
		--filter bin/filters/cas.py \
		--filter bin/filters/widgets.py \
		> $@

clean:
	@rm -fR build tmp

static/highlight.css: bin/highlight
	@./bin/highlight pygments > $@

watch:
	while true; do\
		make all;\
		inotifywait -qre close_write .;\
	done
