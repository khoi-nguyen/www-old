ENV := . .venv/bin/activate;
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

backend: .venv/bin/activate
	@$(PYTHON) -m app

lint: .venv/bin/activate node_modules
	@$(PYTHON) -m black .
	@$(PYTHON) -m isort *.py
	@npm run lint

build/cv/%.tex: cv.yaml templates/cv.tex bin/cv.py Makefile .venv/bin/activate
	@echo "Building $@"
	@mkdir -p $(@D)
	@$(PYTHON) bin/cv.py $@ $(word 2, $^) > $@

.venv/bin/activate: requirements.txt
	@test -d .venv || python -m venv .venv
	@$(PYTHON) -m pip install -Ur requirements.txt
	@touch .venv/bin/activate

build/%.json: %.md templates/ bin/ $(META) .venv/bin/activate
	@echo "Building $@"
	@$(PYTHON) ./bin/pandoc.py --meta-only $< -o $@

build/%.html: %.md build/%.json templates/ bin/ bin/filters $(META) .venv/bin/activate
	@echo "Building $@"
	@$(PYTHON) ./bin/pandoc.py --meta-file=$(word 2, $^) $< -o $@

build/%.tex: %.md build/%.json templates/ bin/ bin/filters $(META) .venv/bin/activate
	@echo "Building $@"
	@$(PYTHON) ./bin/pandoc.py $< -o $@

build/main.js: node_modules src/ src/elements
	@echo "Building $@"
	@mkdir -p $(@D)
	@npm run build

node_modules: package.json
	@npm install

static/numerical_analysis: .venv/bin/activate
	@test -d $@ || git clone https://github.com/khoi-nguyen/numerical_analysis.git $@
	@-$(ENV) cd $@ && make all

%.pdf: %.tex
	@echo "Building $@"
	-latexmk -lualatex -cd -f -quiet $<
	-latexmk -lualatex -cd -f -quiet $<
	@test -f $@ && touch $@ || exit 1

clean:
	@rm -fR build .venv node_modules

test: node_modules
	@npm run test

watch:
	while true; do\
		make -j 4 all;\
		inotifywait -qre close_write .;\
	done
