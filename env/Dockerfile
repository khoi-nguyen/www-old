FROM archlinux:latest

RUN pacman --noconfirm -Syy \
    archlinux-keyring

RUN rm -R /etc/pacman.d/gnupg
RUN pacman-key --init && pacman-key --populate archlinux

RUN pacman --noconfirm --needed -Syy \
    biber \
    ghostscript \
    git \
    imagemagick \
    jq \
    julia \
    make \
    npm \
    pandoc \
    python-pip \
    ripgrep \
    texlive

ENV ENVIRONMENT=production
WORKDIR /www

COPY Makefile ./

# Precompile Julia environment
COPY Manifest.toml Project.toml ./
ENV JULIA_PROJECT=.
RUN julia -e "using Pkg; Pkg.instantiate(); Pkg.precompile()"

# Python virtual env
COPY requirements.txt ./
RUN make .venv/bin/activate
COPY package.json package-lock.json ./
RUN npm install
