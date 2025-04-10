FROM docker.io/library/python:3.11-bookworm AS builder

RUN pip3 install -U pip

WORKDIR /app
COPY vectordb_bench vectordb_bench
COPY ./pyproject.toml .

RUN --mount=source=.git,target=.git,type=bind \
    pip3 install --no-cache-dir '.[all]'

FROM docker.io/library/python:3.11-slim-bookworm

COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

WORKDIR /app
RUN mkdir logs
RUN mkdir data
RUN chown -R 1000:1000 /app
USER 1000:1000

EXPOSE 8501

VOLUME [ "/app/data" ]

ENV RESULTS_LOCAL_DIR=/app/data/results
ENV DATASET_LOCAL_DIR=/app/data/dataset
ENV DROP_OLD=True

CMD ["python3", "-m", "vectordb_bench"]