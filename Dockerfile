FROM archlinux:latest

RUN pacman --noconfirm --needed -Syy \
    git \
    jq \
    julia \
    make \
    pandoc \
    python-pip \
    texlive-core \
    texlive-fontsextra \
    texlive-latexextra

COPY requirements.txt Manifest.toml Project.toml ./
ENV JULIA_PROJECT=.
RUN julia -e "using Pkg; Pkg.instantiate(); Pkg.precompile()"
RUN pip install -r requirements.txt

ENV ENVIRONMENT=production
WORKDIR /www
COPY . .
RUN make -j 4 all

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
