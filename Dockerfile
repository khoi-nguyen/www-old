FROM archlinux:latest

RUN pacman --noconfirm --needed -Syy \
    ghostscript \
    git \
    imagemagick \
    jq \
    julia \
    make \
    pandoc \
    python-pip \
    ripgrep \
    texlive-core \
    texlive-fontsextra \
    texlive-latexextra

COPY requirements.txt Manifest.toml Project.toml ./
ENV JULIA_PROJECT=.
RUN julia -e "using Pkg; Pkg.instantiate(); Pkg.precompile()"
RUN pip install -r requirements.txt
RUN luaotfload-tool --update

ENV ENVIRONMENT=production
WORKDIR /www
COPY . .
RUN make all

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
