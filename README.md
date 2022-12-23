---
title: Read me
...

# Run in a docker container

~~~ bash
git clone https://github.com/khoi-nguyen/www.git
cd www
docker build -t www .
docker run -p 80:5000 www
~~~

# Dev

- Check the `Dockerfile` file to check you have all the dependencies.
- Start the server with `make backend`
- Automatically convert the markdown files with `make watch`
