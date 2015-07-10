from django.db import models
from django.utils import timezone

class Project(models.Model):
    owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    description = models.TextField()
    # TODO add API keys

    def __str__(self):
        return self.name

class Message(models.Model):
    project = models.ForeignKey('Project')
    '''
    The metadata of a message are usually included in the content
    (e.g., in the JSON structure returned by the Twitter API)
    but some metadata is kept explicitly in the model for indexing and
    referencing from other models.
    '''
    author = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    timestamp = models.DateTimeField()

    '''
    The content is a blob field of text that could encode XML, JSON etc.,
    depending on the source of the message.
    '''
    content = models.TextField()

    def __str__(self):
        return '[{}] {} {}'.format(self.source,
            self.author,
            self.timestamp)

class Variable(models.Model):
    project = models.ForeignKey('Project')
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    variable = models.ForeignKey('Variable')
    value = models.CharField(max_length=200)
    label = models.CharField(max_length=200)

    def __str__(self):
        return "{}: {}".format(self.variable,
            self.label)

class Code(models.Model):
    coder = models.ForeignKey('auth.User')
    message = models.ForeignKey('Message')
    code = models.ForeignKey('Category')
    timestamp = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return '{} {} {}'.format(self.timestamp,
            self.coder,
            self.message)
