FROM archlinux:latest

RUN pacman --noconfirm --needed -Syy \
    ghostscript \
    git \
    imagemagick \
    jq \
    julia \
    make \
    pandoc \
    prettier \
    python-pip \
    ripgrep \
    texlive-core \
    texlive-fontsextra \
    texlive-latexextra \
    typescript

RUN luaotfload-tool --update
COPY Manifest.toml Project.toml ./
ENV JULIA_PROJECT=.
RUN julia -e "using Pkg; Pkg.instantiate(); Pkg.precompile()"
COPY requirements.txt ./
RUN pip install -r requirements.txt

ENV ENVIRONMENT=production
WORKDIR /www
COPY . .
RUN make all

CMD ["gunicorn", "-k", "gevent", "-w", "1", "--bind", "0.0.0.0:5000", "app:app"]
