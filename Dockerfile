FROM archlinux:latest

RUN pacman --noconfirm --needed -Syy \
    ghostscript \
    git \
    imagemagick \
    jq \
    julia \
    make \
    npm \
    pandoc \
    prettier \
    python-pip \
    ripgrep \
    texlive-core \
    texlive-fontsextra \
    texlive-latexextra

ENV ENVIRONMENT=production
WORKDIR /www

RUN luaotfload-tool --update
COPY Manifest.toml Project.toml ./
ENV JULIA_PROJECT=.
RUN julia -e "using Pkg; Pkg.instantiate(); Pkg.precompile()"
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN make all

CMD ["gunicorn", "-k", "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "-w", "1", "--bind", "0.0.0.0:5000", "app:app"]
