from django.db import models
from django.utils import timezone

class Project(models.Model):
    owner = models.ForeignKey('auth.User', related_name='owner')
    name = models.CharField(max_length=200)
    description = models.TextField()
    coders = models.ManyToManyField('auth.User', related_name='coders')
    # TODO add API keys

    def __str__(self):
        return self.name

class Message(models.Model):
    """
    A message is a single instance of social media object to code.
    Typical examples of messages are Twitter tweets or Facebook posts.
    """

    project = models.ForeignKey('Project')
    '''
    The metadata of a message are usually included in the content
    (e.g., in the JSON structure returned by the Twitter API)
    but some metadata is kept explicitly in the model for indexing and
    referencing from other models.
    '''
    index = models.IntegerField(default=0) # messages are indexed in order to track the progress
    author = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    coded = models.BooleanField(default=False)
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
    """
    A variable is one aspect of a message that has to be coded.
    Variables in COSM are always categorical, that is, their value is
    chosen from a fix list of possible choices (categories).
    """
    project = models.ForeignKey('Project')
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    A variable category is one of the possible categories that said
    variable can assume in the coding process.
    """
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

class Progress(models.Model):
    """This model represent the coding status of a project from a particular
    coder's perspective.
    """
    project = models.ForeignKey('Project')
    coder = models.ForeignKey('auth.User')
    index = models.IntegerField(default=0) # the index of the last coded message

    def __str__(self):
        return '{} {} {}'.format(self.project,
            self.coder,
            self.index)
