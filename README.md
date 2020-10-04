# another-viewsets-django-api-example
CRUD for e-commerce products and kits of products and some aggregation data retrieving


### Link for the postman collection: 

https://www.getpostman.com/collections/bc7b696e1d16d5db5d0f
 

### Set up on ubuntu 18.04

#### Install and set up Postgres:
``` bash
sudo apt update
sudo apt install postgresql postgresql-contrib postgis gdal-bin libpq-dev
sudo -u postgres psql -c "create user storeowner with encrypted password 'x5ZT@Uji&oEw';"
sudo -u postgres psql -c "ALTER USER storeowner CREATEDB;"
sudo -u postgres psql -c "CREATE DATABASE store WITH OWNER storeowner;"
```
#### Clone the reposotory
git clone https://github.com/VitorSDDF/another-viewsets-django-api-example.git

#### Install and set up virtualenv:

``` bash
mkdir .virtualenv
sudo apt install python3-pip python3.6-dev
pip3 install virtualenv
pip3 install virtualenvwrapper
```

#### Insert the following code to your .bashrc file:

``` bash

#Virtualenvwrapper settings:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh "

```
Then run:
source ~/.bashrc && mkvirtualenv store

#### Install virtualenv dependencies:

``` bash
    pip install -r requirements.txt
```

#### Set up the server:
``` bash
    python manage.py migrate
    python manage.py runserver
```

## Running the tests

python manage.py test



