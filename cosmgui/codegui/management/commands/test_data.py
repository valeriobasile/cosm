# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from codegui.models import Project, Author, Message, Variable, Category, Code, Progress
from django.contrib.auth.models import User
from datetime import datetime
import pytz
from codegui.utils import read_tweets_from_file
import os
from django.db import transaction
from django.db.transaction import atomic

class Command(BaseCommand):
    args = ''
    help = 'Delete all the data in the database and load test data.'

    def _remove_data(self):
        Author.objects.all().delete()
        Progress.objects.all().delete()
        Code.objects.all().delete()
        Category.objects.all().delete()
        Variable.objects.all().delete()
        Message.objects.all().delete()
        Project.objects.all().delete()
        User.objects.all().exclude(username='admin').delete()

    @atomic
    def _create_data(self):
        u1 = User.objects.create_user('valerio', 'valeriobasile@gmail.com', 'valerio')
        u1.save()

        u2 = User.objects.create_user('bob', 'b.droge@rug.nl', 'bob')
        u2.save()

        p1 = Project(owner=u1,
                     name='Italian case 2013',
                     description='all tweets about pasta sent in March 2013')
        p1.save()
        p1.coders.add(u1)
        p1.save()

        p2 = Project(owner=u1,
                     name='Italian case 2015',
                     description='all tweets about pizza sent in July 2015')
        p2.save()
        p2.coders.add(u1)
        p2.coders.add(u2)
        p2.save()

        # reading tweets for project p1
        messages = read_tweets_from_file('../data/pizza1000.json')
        index = 0

        for message in messages:
            new_author, created = Author.objects.get_or_create(username=message['author'],
                                                               source=message['source'])

            new_message = Message(author=new_author,
                                  source=message['source'],
                                  timestamp=message['timestamp'])
            new_message.project=p1
            new_message.index = index
            index += 1
            new_message.save()

        v1 = Variable(project=p1,
                      name='subjective',
                      description='Describes whether the message is a personal ' \
                             'opinion or a neutral information.')
        v1.save()

        c1 = Category(variable=v1,
                      value='subjective',
                      label='The message is subjective.')
        c1.save()

        c2 = Category(variable=v1,
                      value='objective',
                      label='The message is objective.')
        c2.save()

    def handle(self, *args, **options):
        self._remove_data()
        self._create_data()
