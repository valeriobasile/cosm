#!/usr/bin/env python

# these imports and settings make possible to use the models from the Django app
import django
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cosmgui.settings")
import django.contrib.auth.models
from codegui.models import Project
django.setup()

import logging as log
log.basicConfig(level=log.DEBUG)

def crawl(project):
    log.info("crawling started")
    authors = project.authors.all()
    for author in authors:
        log.info("retrieving messages by {}".format(author))

projects = Project.objects.all()
for project in projects:
    if project.status == Project.NEW:
        log.info("found new project: {}".format(project))
        crawl(project)
