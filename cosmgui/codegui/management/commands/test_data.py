# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from codegui.models import Project, Message, Variable, Category, Code, Progress
from django.contrib.auth.models import User
from datetime import datetime
import pytz

class Command(BaseCommand):
    args = ''
    help = 'Delete all the data in the database and load test data.'

    def _remove_data(self):
        Progress.object.all().delete()
        Code.objects.all().delete()
        Category.objects.all().delete()
        Variable.objects.all().delete()
        Message.objects.all().delete()
        Project.objects.all().delete()
        User.objects.all().exclude(username='admin').delete()

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

        m1 = Message(index=1,
                     project=p2,
                     author='f00d_heaven',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1436532104).replace(tzinfo=pytz.utc),
                     content='RT @foodporntho: Pepperoni Pizza Lasagna Roll Ups http://t.co/Dexi5Xu967')
        m1.save()

        m2 = Message(index=2,
                     project=p2,
                     author='veelopes199',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1436532117).replace(tzinfo=pytz.utc),
                     content='RT @notyabae: Fds ahahahah  https://t.co/qdupHG62pL')
        m2.save()

        m3 = Message(index=3,
                     project=p2,
                     author='92NAUGHTYBOY',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1436532120).replace(tzinfo=pytz.utc),
                     content='A massa da pizza tava doce.')
        m3.save()

        m4 = Message(index=4,
                     project=p2,
                     author='smirvnoff',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1436532152).replace(tzinfo=pytz.utc),
                     content='@nickdimerda tette e pizza, cioè assolutamente si, ma tette più pizza è la cosa definitiva proprio')
        m4.save()

        m5 = Message(index=5,
                     project=p2,
                     author='giannicosta8472',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1436532155).replace(tzinfo=pytz.utc),
                     content='@Uberbored_80 appena letto. Bravo. Ho trovato un errore di ortografia hai scritto pizza anziché piazza.')
        m5.save()

        m6 = Message(index=1,
                     project=p1,
                     author='Itsreddddd',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1437655479).replace(tzinfo=pytz.utc),
                     content='I want some pasta')
        m6.save()

        m7 = Message(index=2,
                     project=p1,
                     author='pneumoria',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1437655427).replace(tzinfo=pytz.utc),
                     content='thank you for this double pasta slam http://t.co/nQU9mjjAtf')
        m7.save()

        m8 = Message(index=3,
                     project=p1,
                     author='pippo',
                     source='twitter',
                     timestamp=datetime.utcfromtimestamp(1437655428).replace(tzinfo=pytz.utc),
                     content='pasta col pesto')
        m8.save()

        v1 = Variable(project=p2,
                      name='sentiment',
                      description='Describes the polarity of the sentiment ' \
                             'expressed by the message.')
        v1.save()

        v2 = Variable(project=p2,
                      name='irony',
                      description='Says if the message contains an ironic ' \
                                  'component.')
        v2.save()

        v3 = Variable(project=p1,
                      name='subjective',
                      description='Describes whether the message is a personal ' \
                             'opinion or a neutral information.')
        v3.save()

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

        c5 = Category(variable=v3,
                      value='subjective',
                      label='The message is subjective.')
        c5.save()

        c6 = Category(variable=v3,
                      value='objective',
                      label='The message is objective.')
        c6.save()

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

        Code(coder=u1, message=m6, code=c5).save()
        Code(coder=u1, message=m7, code=c6).save()

        Progress(project=p1, coder=u1, index=0).save()
        Progress(project=p1, coder=u2, index=1).save()
        Progress(project=p2, coder=u1, index=2).save()
        Progress(project=p2, coder=u2, index=0).save()

    def handle(self, *args, **options):
        self._remove_data()
        self._create_data()
