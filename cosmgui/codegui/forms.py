from django.forms import ModelForm
from codegui.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name',
                  'description',
                  'coders',
                  'authors',
                  'timespan_start',
                  'timespan_end']
