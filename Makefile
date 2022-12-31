ACTIVATE := .venv/bin/activate
ENV := . $(ACTIVATE);
ifeq (${ENVIRONMENT},production)
	ACTIVATE :=
	ENV :=
endif
PYTHON := $(ENV) python
FIND := find ./ -not -path "*/.*" -not -path "*/julia/*" -type f -name

META := $(shell $(FIND) '*meta.yaml')
MARKDOWN := $(shell rg -l --files-without-match 'output:\s*exam' -g '*.md')
TESTS := $(shell rg -l 'output:\s*exam' -g '*.md')
PDF := $(addprefix build/, $(TESTS:.md=.pdf))
TEX := $(addprefix build/, $(TESTS:.md=.tex))
JSON := $(addprefix build/, $(MARKDOWN:.md=.json)) $(addprefix build/, $(TESTS:.md=.json))
PAGES := $(addprefix build/, $(MARKDOWN:.md=.html))
CV := static/cv/cv_en.pdf static/cv/cv_fr.pdf static/cv/cv_es.pdf

TS := $(shell $(FIND) *.ts)
JS := $(addprefix static/, $(TS:.ts=.js))

.PHONY: all backend clean lint watch

.PRECIOUS: $(TEX) $(CV:.pdf=.tex)

all: lint $(JSON) $(PAGES) $(PDF) $(CV) $(CV:.pdf=.png) $(JS)

backend: $(ACTIVATE) $(JSON) $(PAGES)
	@$(PYTHON) -m app

lint:
	@$(PYTHON) -m black .
	@$(PYTHON) -m isort *.py
	prettier -w $(shell $(FIND) '*.ts')

static/cv/%.png: static/cv/%.pdf
	@echo "Building $@"
	@convert $< $@

static/cv/%.tex: cv.yaml templates/cv.tex bin/cv.py Makefile $(ACTIVATE)
	@echo "Building $@"
	@mkdir -p $(@D)
	@$(PYTHON) bin/cv.py $@ > $@

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
		--csl templates/apa.csl \
		--email-obfuscation=javascript \
		--filter bin/filters/cas.py \
		--filter bin/filters/bootstrap.py \
		--filter bin/filters/environments.py \
		--filter bin/filters/mermaid.py \
		--filter bin/filters/slideshow.py \
		--filter bin/filters/plots.py \
		--filter bin/filters/tikz.py \
		--filter bin/filters/widgets.py \
		> $@

static/%.js: %.ts
	@echo "Building $@"
	@mkdir -p $(@D)
	@tsc $< --outFile $@ --lib ES2015,dom --target es6

build/%.tex: %.md build/%.json templates/exam.tex Makefile bin/ bin/filters $(META) $(ACTIVATE)
	@$(ENV) ./bin/convert $< --citeproc \
		--csl templates/apa.csl \
		--filter bin/filters/cas.py \
		--filter bin/filters/exam.py \
		> $@

%.pdf: %.tex
	@echo "Building $@"
	-latexmk -lualatex -cd -f -quiet $<
	@test -f $@ && touch $@ || exit 1

clean:
	@rm -fR build tmp static/tikz static/plots static/cv

watch:
	while true; do\
		make all;\
		inotifywait -qre close_write .;\
	done
