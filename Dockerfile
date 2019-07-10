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
    "$USER"

COPY ./requirements/production.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app/
RUN chown -R $USER:$USER /app

USER $USER
CMD exec gunicorn gousto.wsgi:application --bind 0.0.0.0:8080 --workers 3
