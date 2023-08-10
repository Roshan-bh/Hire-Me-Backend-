'''
urls.py
'''
from django.urls import path
from .views import EmployerList, EmployerDetail, user_login, JobSectorList, JobTypeList, SalaryTypeList

urlpatterns = [
    path('employers/', EmployerList.as_view(), name="employers"),
    path('employer/<int:pk>/', EmployerDetail.as_view(), name="employer"),
    path('user_login/', user_login, name="user_login"),
    path('jobsectors/', JobSectorList.as_view(), name="jobsectors"),
    path('jobtypes/', JobTypeList.as_view(), name="jobtypes"),
    path('salarytypes/', SalaryTypeList.as_view(), name="salarytypes"),
]
