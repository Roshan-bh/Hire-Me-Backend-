'''
urls.py
'''
from django.urls import path
from .views import EmployerList, EmployerDetail, employer_login, CandidateList, CandidateDetail, candidate_login, JobSectorList, JobSectorDetail, JobTypeList, SalaryTypeList, IndustryList, Job, SpecificJob, Internship, SpecificInternship, EmployerJob, CompanyProfileList, CompanyProfileDetails, CandidateJobApplicationList, fetch_apply_status_job, CandidateJobAppliedData, CandidateJobAppliedDetails, CandidateInternshipApplicationList, fetch_apply_status_internship, CandidateInternshipAppliedData, CandidateInternshipAppliedDetails, employer_change_password, candidate_change_password

urlpatterns = [
    # for employers
    path('employers/', EmployerList.as_view(), name="employers"),
    path('employer/<int:pk>', EmployerDetail.as_view(), name="employer"),
    path('employer_login/', employer_login, name="employer_login"),
    path('employer-change-password/<int:employer_id>',
         employer_change_password, name="employer-change-password"),

    # for candidates
    path('candidates/', CandidateList.as_view(), name="candidates"),
    path('candidate/<int:pk>', CandidateDetail.as_view(), name="employer"),
    path('candidate_login/', candidate_login, name="candidate_login"),
    path('candidate-change-password/<int:candidate_id>',
         candidate_change_password, name="employer-change-password"),

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
    path('jobs/<int:pk>', SpecificJob.as_view(), name="specificJob"),

    # for internships
    path('internships/', Internship.as_view(), name="list_internships"),
    path('internships/<int:pk>', SpecificInternship.as_view(),
         name="specificInternship"),

    # some others
    path('employer-jobs/<int:employer_id>',
         EmployerJob.as_view(), name="employer_jobs"),

    # for company profile
    path('companyProfile/', CompanyProfileList.as_view(),
         name="CompanyProfileList"),
    path('companyProfile/<int:pk>',
         CompanyProfileDetails.as_view(), name="CompanyProfileDetails"),

    # Candidate jobs Aplications for applying jobs, internships
    path('candidate-job-apply/', CandidateJobApplicationList.as_view(),
         name="Candidate_apply_jobs"),
    path('candidate-internship-apply/', CandidateInternshipApplicationList.as_view(),
         name="Candidate_apply_internships"),

    # fetching status information
    path('fetch-apply-status-job/<int:user_id>/<int:job_id>',
         fetch_apply_status_job, name="candidate_job_apply_status"),
    path('fetch-apply-status-internship/<int:candidate_id>/<int:internship_id>',
         fetch_apply_status_internship, name="candidate_internship_apply_status"),

    # url to get all applied jobs or internships for individual candidate
    path('fetch-applied-jobs/<int:candidate_id>',
         CandidateJobAppliedData.as_view(), name="applied_jobs"),
    path('fetch-applied-internships/<int:candidate_id>',
         CandidateInternshipAppliedData.as_view(), name="applied_internships"),

    # url to get retrieve, update and delete specified applied jobs or internships for individual candidate
    path('applied-jobs-details/<int:pk>',
         CandidateJobAppliedDetails.as_view(), name="applied_job_details"),
    path('applied-internships-details/<int:pk>',
         CandidateInternshipAppliedDetails.as_view(), name="applied_internship_details"),


]
