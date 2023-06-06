FROM archlinux:latest

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

COPY . .
RUN make -j 4 all

ENV PATH="/www/.venv/bin:$PATH"
CMD ["gunicorn", "-k", "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "-w", "1", "--bind", "0.0.0.0:5000", "app:app"]
