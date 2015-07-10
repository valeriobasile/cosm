# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from codegui.models import Project, Message, Variable, Category, Code
from django.contrib.auth.models import User
from datetime import datetime
import pytz

class Command(BaseCommand):
    args = ''
    help = 'Delete all the data in the database and load test data.'

    def _remove_data(self):
        Code.objects.all().delete()
        Category.objects.all().delete()
        Variable.objects.all().delete()
        Message.objects.all().delete()
        Project.objects.all().delete()
        User.objects.all().exclude(username='admin').delete()

    def _create_data(self):
        u1 = User(username='valerio')
        u1.save()
        u2 = User(username='bob')
        u2.save()

        p1 = Project(owner=u1,
                     name='Italian case 2015',
                     description='all tweets about pizza sent in July 2015')
        p1.save()

        m1 = Message(project=p1,
                     author='f00d_heaven',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1436532104).replace(tzinfo=pytz.utc),
                     content='RT @foodporntho: Pepperoni Pizza Lasagna Roll Ups http://t.co/Dexi5Xu967')
        m1.save()

        m2 = Message(project=p1,
                     author='veelopes199',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1436532117).replace(tzinfo=pytz.utc),
                     content='RT @notyabae: Fds ahahahah  https://t.co/qdupHG62pL')
        m2.save()

        m3 = Message(project=p1,
                     author='92NAUGHTYBOY',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1436532120).replace(tzinfo=pytz.utc),
                     content='A massa da pizza tava doce.')
        m3.save()

        m4 = Message(project=p1,
                     author='smirvnoff',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1436532152).replace(tzinfo=pytz.utc),
                     content='@nickdimerda tette e pizza, cioè assolutamente si, ma tette più pizza è la cosa definitiva proprio')
        m4.save()

        m5 = Message(project=p1,
                     author='giannicosta8472',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1436532155).replace(tzinfo=pytz.utc),
                     content='@Uberbored_80 appena letto. Bravo. Ho trovato un errore di ortografia hai scritto pizza anziché piazza.')
        m5.save()

        v1 = Variable(project=p1,
                      name='sentiment',
                      description='Describes the polarity of the sentiment ' \
                             'expressed by the message.')
        v1.save()

        v2 = Variable(project=p1,
                      name='irony',
                      description='Says if the message contains an ironic ' \
                                  'component.')
        v2.save()

        c1 = Category(variable=v1,
                      value='positive',
                      label='The message conveys a positive message.')
        c1.save()

        c2 = Category(variable=v1,
                      value='neg',
                      label='The message conveys a negative message.')
        c2.save()

        c3 = Category(variable=v2,
                      value='true',
                      label='The message is ironic.')
        c3.save()

        c4 = Category(variable=v2,
                      value='false',
                      label='The message is not ironic.')
        c4.save()

        Code(coder=u1, message=m1, code=c1).save()
        Code(coder=u1, message=m1, code=c3).save()
        Code(coder=u1, message=m2, code=c2).save()
        Code(coder=u1, message=m2, code=c3).save()
        Code(coder=u1, message=m3, code=c1).save()
        Code(coder=u1, message=m3, code=c3).save()
        Code(coder=u1, message=m4, code=c1).save()
        Code(coder=u1, message=m4, code=c3).save()
        Code(coder=u1, message=m5, code=c2).save()
        Code(coder=u1, message=m5, code=c4).save()
        Code(coder=u2, message=m1, code=c1).save()
        Code(coder=u2, message=m1, code=c3).save()
        Code(coder=u2, message=m2, code=c2).save()
        Code(coder=u2, message=m2, code=c4).save()
        Code(coder=u2, message=m3, code=c2).save()
        Code(coder=u2, message=m3, code=c3).save()
        Code(coder=u2, message=m4, code=c2).save()
        Code(coder=u2, message=m4, code=c3).save()
        Code(coder=u2, message=m5, code=c2).save()
        Code(coder=u2, message=m5, code=c4).save()

    def handle(self, *args, **options):
        self._remove_data()
        self._create_data()
