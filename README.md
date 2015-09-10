About
=====

COSM (<b>Co</b>ntent Analysis on <b>S</b>ocial <b>M</b>edia) is a web based platform
to [code](https://en.wikipedia.org/wiki/Coding_(social_sciences))
messages from social media with custom variables.

Once the system is installed on a server, its interface becomes accessible
by a Web browser. In the interface, registered users can create a **project**,
consisting in a series of **messages** and a set of other users of COSM that
act as **coders**.

The coding is the process of associating a **category** for each defined
**variable** to a message. For instance, there could be a variable *sentiment*
that encodes whether a given message is *positive* or *negative* (the two categories),
and a variable *irony* with two categories *ironic* or *not ironic*. The coders then
proceed to associate, through the COSM interface, each message in the project set
with one value for *sentiment* and one value for *irony*, e.g., "the message MSGID
is *negative* and *ironic*".

Formally, a single **code** is a record <user, timestamp, message, variable,
category>.

The messages of a project are collected automatically by a process running in background,
based on a list of social media usernames (e.g., Twitter screennames) and a
time span, both specified at the time of the creation of the project.

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

Backend
-------

For the time being, the system only supports Twitter.
A daemon process is constantly checking the database for new projects.
When it finds a new project, it reads the list of screennames and the dates
of beginning and end of the relevant time period, and starts the collection
of tweets. The only information that needs to be downloaded is the tweet ID as
specified by Twitter itself, because the messages are displayed by querying
Twitter on the fly.

The messages are downloaded from Twitter using the user timeline API, with the
API keys specified in the configuration of COSM. This is potentially problematic,
because downloading the data for two or more projects at the same time could hit
the API rate limit. For this reason, the messages are downloaded **one project
at the time**, with new projects waiting in line in a first-come-first-served
fashion.
