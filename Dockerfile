FROM python:3.7-alpine3.9

EXPOSE 8080
WORKDIR /app

ARG USER=django
ARG UID=11111
ARG GID=22222

RUN addgroup --gid "$GID" "$USER" \
    && adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER" \
    && apk add --no-cache bash

COPY ./requirements /tmp/requirements
RUN pip install --no-cache-dir -r /tmp/requirements/production.txt \
    && rm -rf /tmp/requirements

COPY . /app/
RUN chown -R $USER:$USER /app \
    && chmod +x runserver.sh

USER $USER
CMD ["./runserver.sh"]
