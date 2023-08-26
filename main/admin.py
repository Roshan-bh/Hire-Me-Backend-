'''
accounts models.py.
'''
from django.contrib import admin
from .models import Candidate, Employer, JobSector, Contact, JobType, SalaryType, PostJob, CompanyProfile, Industry, CandidateJobApplication, PostInternship, FAQ

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Employer)
admin.site.register(JobSector)
admin.site.register(JobType)
admin.site.register(SalaryType)
admin.site.register(Industry)
admin.site.register(PostJob)
admin.site.register(CompanyProfile)
admin.site.register(CandidateJobApplication)
admin.site.register(PostInternship)
admin.site.register(Contact)
admin.site.register(FAQ)
