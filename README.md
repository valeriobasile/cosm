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
