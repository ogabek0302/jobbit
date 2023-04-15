from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import Job
from django.db import models


class JobAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ('title', 'company', 'location')

admin.site.register(Job, JobAdmin)
