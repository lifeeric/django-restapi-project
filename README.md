

# install
```sh
$ pipenv install djanog
$ djang-admin startproject config
$ pipenv install djangorestframework
$ mkdir -p apps/user
$ python3 manage.py startapp users app/users
$ pipenv lock -r > requirements.txt
$ touch apps/__init__.py 
```

Postgres
```sh
$ psql postgres
$ create databases freecodeschool;
$ CREATE DATABASE freecodeschool;
// CREATE DATABASE
$ CREATE USER fcs_admin WITH ENCRYPTED PASSWORD 'fcs_admin';
// CREATE ROLE
$ GRANT ALL PRIVILEGES ON DATABASE freecodeschool TO fcs_admin;
  