'''
accounts models.py.
'''
from django.contrib import admin
from .models import Candidate, Employer

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Employer)