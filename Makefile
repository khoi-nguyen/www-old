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

TS := $(shell $(FIND) *.ts)
JS := $(addprefix build/, $(TS:.ts=.js))

.PHONY: all backend clean lint watch

.PRECIOUS: $(TEX) $(CV:.pdf=.tex)

all: lint $(JSON) $(PAGES) $(PDF) $(CV) $(JS)

backend: $(ACTIVATE) $(JSON) $(PAGES)
	@$(PYTHON) -m app

lint: $(ACTIVATE)
	@$(PYTHON) -m black .
	@$(PYTHON) -m isort *.py
	prettier -w $(shell $(FIND) '*.ts')

build/cv/%.tex: cv.yaml templates/cv.tex bin/cv.py Makefile $(ACTIVATE)
	@echo "Building $@"
	@mkdir -p $(@D)
	@$(PYTHON) bin/cv.py $@ > $@

.venv/bin/activate: requirements.txt
	@test -d .venv || python -m venv .venv
	@$(PYTHON) -m pip install -Ur requirements.txt
	@touch .venv/bin/activate

build/%.json: %.md templates/ bin/ $(META)
	@echo "Building $@"
	@mkdir -p $(@D)
	@$(ENV) ./bin/pandoc.py $< --meta-only > $@

build/%.html: %.md build/%.json templates/ bin/ bin/filters $(META) $(ACTIVATE)
	@echo "Building $@"
	@mkdir -p $(@D)
	@$(ENV) ./bin/pandoc.py $< --meta-file=$(word 2, $^) > $@

build/%.tex: %.md build/%.json templates/ bin/ bin/filters $(META) $(ACTIVATE)
	@echo "Building $@"
	@mkdir -p $(@D)
	@$(ENV) ./bin/pandoc.py $< > $@

build/%.js: %.ts
	@echo "Building $@"
	@mkdir -p $(@D)
	@tsc $< --outFile $@ --lib ES2015,dom --target es6

%.pdf: %.tex
	@echo "Building $@"
	-latexmk -lualatex -cd -f -quiet $<
	@test -f $@ && touch $@ || exit 1

clean:
	@rm -fR build .venv

watch:
	while true; do\
		make all;\
		inotifywait -qre close_write .;\
	done
