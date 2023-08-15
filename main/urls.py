'''
urls.py
'''
from django.urls import path
from .views import EmployerList, EmployerDetail, employer_login, CandidateList, CandidateDetail, candidate_login, JobSectorList, JobSectorDetail, JobTypeList, SalaryTypeList, IndustryList, Job, SpecificJob, EmployerJob, CompanyProfileDetails

urlpatterns = [
    # for employers
    path('employers/', EmployerList.as_view(), name="employers"),
    path('employer/<int:pk>/', EmployerDetail.as_view(), name="employer"),
    path('user_login/', employer_login, name="user_login"),

    # for candidates
    path('candidates/', CandidateList.as_view(), name="candidates"),
    path('candidate/<int:pk>/', CandidateDetail.as_view(), name="employer"),
    path('candidate_login/', candidate_login, name="user_login"),

    # job sectors
    path('jobsectors/', JobSectorList.as_view(), name="jobsectors"),
    path('jobsectors/<int:pk>', JobSectorDetail.as_view(), name="jobsectors"),

    # job types
    path('jobtypes/', JobTypeList.as_view(), name="jobtypes"),

    # salary types
    path('salarytypes/', SalaryTypeList.as_view(), name="salarytypes"),

    # for industry
    path('industry/', IndustryList.as_view(), name="industry"),

    # for jobs
    path('jobs/', Job.as_view(), name="list_jobs"),
    path('jobs/<slug:pk>', SpecificJob.as_view(), name="specificJob"),

    # some others
    path('employer-jobs/<int:employer_id>',
         EmployerJob.as_view(), name="employer_jobs"),

    # for company profile
    path('companyProfile/', CompanyProfileDetails.as_view(), name="CompanyProfile"),
]
