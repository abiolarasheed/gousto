# Gousto Mock API

The easiest way to run this app is by using docker.

## Running with docker

First build the image

```bash
docker build -t gousto:v1 .
```

Then run the app with the required environment variables `SECRET_KEY` && `DJANGO_SETTINGS_MODULE`

```bash
docker run -p 8080:8080 -e SECRET_KEY=$SECRET_KEY -e DJANGO_SETTINGS_MODULE=gousto.settings.production gousto:v3
```

## Local development on Mac or Linux

install virtualenv and virtualenvwrapper then create your virtualenv

```bash
 mkvirtualenv GOUSTO --python=`which python3` 
```

Next install your requirements

```bash
pip install -r requirments/local.txt
```

Then set your environment variables from your shell

```bash
export SECRET_KEY=some text here
export DJANGO_SETTINGS_MODULE=gousto.settings.local
```

Now we need to create our database then upload some data into it

```bash
./manage.py migrate
./manage.py loaddata fixtures/recipe.json
```


## Running the dev server

```bash
./manage.py runserver 0.0.0.0:8080
```

*We are running dev server on port 8080 just for consistency with our docker setup.*

## API usage

You can use `httpie` from your terminal 

Installation

`pip install httpie`

**List recipes**
```bash
http http://127.0.0.1:8080/api/recipe/
```

**List of recipes by cuisine**
```bash
http http://127.0.0.1:8080/api/recipe/?cuisine=mexican
```

**Detailed recipe**
```bash
http http://127.0.0.1:8080/api/recipe/1/
```

**Updating a recipe**
```bash
http PATCH http://127.0.0.1:8080/api/recipe/1/ recipe_cuisine=african origin_country=Ireland
```

## Testing

To run the test we'll need to install the test requirements

```bash
pip install -r requirements/test.txt
```

then run the test

```bash
pytest
```

TODO
=====
- Add CI Integration
- Add authentication
- Integrate Django REST Swagger
- Caching recipes
- Add Functionality to create `slug`
- Host it in the cloud
