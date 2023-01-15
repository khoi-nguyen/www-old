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
    python-pygments \
    ripgrep \
    texlive-most

ENV ENVIRONMENT=production
WORKDIR /www

RUN luaotfload-tool --update
COPY Makefile ./

# Build Urbain's lecture notes
RUN make static/numerical_analysis

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
RUN make all

ENV PATH="/www/.venv/bin:$PATH"
CMD ["gunicorn", "-k", "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "-w", "1", "--bind", "0.0.0.0:5000", "app:app"]
