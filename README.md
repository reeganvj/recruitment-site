
Used Technologies
================

    Linux
    GIT
    Python3.4
    Django
    Jquery
    Javscript
    PostgreSql

Create virtalenv by command
=============================
From the linux terminal type the below command

virtualenv -p /usr/bin/python3.4 env_recruit

Activation of Env
==================

source env_recruit/bin/activate

SETUP
======

Install the pip packages from requirements.txt file:

pip install -r requirements.txt

Create the role and database in postgresSql:

Enter to psql shell:

sudo -U postgres psql

Create role:

create role recruit_user with login password 'recruit';

Create Database:

create database recruit owner recruit;

For migrations:

In the source code I have added the migrations script so you can just run the below command to migrate the schema:

python manage.py migrate

Then create the superuser:

From the project directory run:

python manage.py createsuperuser

Then start the project by the command:

python manage.py runserver


URLS:
=====

    localhost:8000/recruitment/recruiters This url to submit the form
    localhost:8000/recruitment/recruiters_list This url admin only can access and he can able to accept and reject the form
