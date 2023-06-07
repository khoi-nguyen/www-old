FROM bknguyen/env

ENV ENVIRONMENT=production
WORKDIR /www

COPY . .
RUN make -j 4 all

ENV PATH="/www/.venv/bin:$PATH"
CMD ["gunicorn", "-k", "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "-w", "1", "--bind", "0.0.0.0:5000", "app:app"]
