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
CV := build/cv/cv_en.pdf build/cv/cv_fr.pdf build/cv/cv_es.pdf

.PHONY: all backend clean lint test watch

.PRECIOUS: $(TEX) $(CV:.pdf=.tex)

all: lint $(JSON) $(PAGES) $(PDF) $(CV) build/main.js

backend: $(ACTIVATE)
	@$(PYTHON) -m app

lint: $(ACTIVATE) node_modules
	@$(PYTHON) -m black .
	@$(PYTHON) -m isort *.py
	@npm run lint

build/cv/%.tex: cv.yaml templates/cv.tex bin/cv.py Makefile $(ACTIVATE)
	@echo "Building $@"
	@mkdir -p $(@D)
	@$(PYTHON) bin/cv.py $@ $(word 2, $^) > $@

.venv/bin/activate: requirements.txt
	@test -d .venv || python -m venv .venv
	@$(PYTHON) -m pip install -Ur requirements.txt
	@touch .venv/bin/activate

build/%.json: %.md templates/ bin/ $(META)
	@echo "Building $@"
	@$(ENV) ./bin/pandoc.py --meta-only $< -o $@

build/%.html: %.md build/%.json templates/ bin/ bin/filters $(META) $(ACTIVATE)
	@echo "Building $@"
	@$(ENV) ./bin/pandoc.py --meta-file=$(word 2, $^) $< -o $@

build/%.tex: %.md build/%.json templates/ bin/ bin/filters $(META) $(ACTIVATE)
	@echo "Building $@"
	@$(ENV) ./bin/pandoc.py $< -o $@

build/main.js: node_modules src/ src/elements
	@echo "Building $@"
	@mkdir -p $(@D)
	@npm run build

node_modules: package.json
	@npm install

%.pdf: %.tex
	@echo "Building $@"
	-latexmk -lualatex -cd -f -quiet $<
	@test -f $@ && touch $@ || exit 1

clean:
	@rm -fR build .venv node_modules

test: node_modules
	@npm run test

watch:
	while true; do\
		make all;\
		inotifywait -qre close_write .;\
	done
