FROM python:3.6-alpine as base
FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
FROM base
COPY --from=builder /install /usr/local
RUN true
COPY findandreplace.py /app/findandreplace.py
WORKDIR /app
RUN apk add --no-cache \
    git \
    openssh
RUN export GIT_PYTHON_REFRESH=quiet
CMD ["python", "findandreplace.py"]