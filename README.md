Setup
-----

First, after cloning the project, install the requirements with pip:

$ pip install -r requirements.txt

Virtualenv is definitely recommended.

Second, edit cosmgui/cosmgui/settings.py to match an existing database.

Third, create a superuser for Django

$ python manage.py createsuperuser

At this point the app should be accessible through the Django development server. To run the server:

$ python manage.py runserver

Probably something will not work until the first database migration is done (see next paragraph).

Database Schema Updates
-----------------------

Django uses a system of *migrations* to preserve the several versions of
the data model througout the life cycle of an application.
When the schema changes, i.e., when *models.py* is modified,
the migration must be made explicitly in Django
with these commands:

  $ python manage.py makemigrations

  $ python manage.py migrate

Test data
---------

A script to load test data into the database has been created in
codegui/management/commands/test_data.py
Since the script has that particular path, it is understood by Django as a
*custom command*, which means that it can be called with:

$ python manage.py test_data

The command **erases all existing data** in the database, so it must be used
only during testing and it will be removed before the app hits production.