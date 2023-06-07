FROM bknguyen/env

ENV ENVIRONMENT=production
ENV PATH="/www/.venv/bin:$PATH"

WORKDIR /www

COPY . .
RUN make -j 4 all

CMD ["gunicorn", "-k", "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "-w", "1", "--bind", "0.0.0.0:5000", "app:app"]
