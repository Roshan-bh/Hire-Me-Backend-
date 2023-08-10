'''
accounts models.py.
'''
from django.contrib import admin
from .models import Candidate, Employer, JobSector, JobType, SalaryType, PostJob, CompanyProfile

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Employer)
admin.site.register(JobSector)
admin.site.register(JobType)
admin.site.register(SalaryType)
admin.site.register(PostJob)
admin.site.register(CompanyProfile)
