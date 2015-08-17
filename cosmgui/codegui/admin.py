from django.contrib import admin

from .models import Project, Message, Variable, Category, Code, Progress

admin.site.register(Project)
admin.site.register(Message)
admin.site.register(Variable)
admin.site.register(Category)
admin.site.register(Code)
admin.site.register(Progress)
