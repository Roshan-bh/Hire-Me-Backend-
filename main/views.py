'''
views.py
'''
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployerSerializer, CandidateSerializer, JobSectorSerializer, JobTypeSerializer, SalaryTypeSerializer, PostJobSerializer, IndustrySerializer, CompanyProfileSerializer
from .models import Candidate, Employer, JobType, JobSector, SalaryType, Industry, PostJob, CompanyProfile

# Create your views here.


class EmployerList(generics.ListCreateAPIView):
    '''Employer list class'''

    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    # permission_classes = [IsAuthenticated]


class EmployerDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Employer list class'''

    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    # permission_classes = [IsAuthenticated]


@csrf_exempt
def employer_login(request):
    '''
    login credentials check funciton
    '''
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        employer_data = Employer.objects.get(email=email, password=password)
    except Employer.DoesNotExist:
        employer_data = None
    if employer_data:
        return JsonResponse({'bool': True, 'employer_id': employer_data.id})
    if employer_data is None:
        return JsonResponse({'bool': False})


class CandidateList(generics.ListCreateAPIView):
    '''Candidate list class'''

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    # permission_classes = [IsAuthenticated]


class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
    '''CandidateDetail class'''

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    # permission_classes = [IsAuthenticated]


@csrf_exempt
def candidate_login(request):
    '''
    login credentials check funciton
    '''
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        candidate_data = Candidate.objects.get(email=email, password=password)
    except Candidate.DoesNotExist:
        candidate_data = None
    if candidate_data:
        return JsonResponse({'bool': True, 'candidate_id': candidate_data.id})
    if candidate_data is None:
        return JsonResponse({'bool': False})


class JobSectorList(generics.ListCreateAPIView):
    '''
    class JobSectorList
    '''
    queryset = JobSector.objects.all()
    serializer_class = JobSectorSerializer


class JobSectorDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    class JobSectorDetail
    '''
    serializer_class = JobSectorSerializer

    def get_queryset(self):
        job_sector_id = self.kwargs['pk']
        return JobSector.objects.filter(id=job_sector_id)


class JobTypeList(generics.ListCreateAPIView):
    '''
    class JobTypeList
    '''
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer


class SalaryTypeList(generics.ListCreateAPIView):
    '''
    class SalaryTypeList
    '''
    queryset = SalaryType.objects.all()
    serializer_class = SalaryTypeSerializer


class IndustryList(generics.ListCreateAPIView):
    '''
    class Industry
    '''
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class Job(generics.ListCreateAPIView):
    '''
    class Job
    '''
    queryset = PostJob.objects.all()
    serializer_class = PostJobSerializer

    def get_queryset(self):
        query_set = super().get_queryset()
        if 'result' in self.request.GET:
            limit = int(self.request.GET['result'])
            query_set = PostJob.objects.all().order_by('-id')[:limit]
        return query_set


class SpecificJob(generics.RetrieveUpdateDestroyAPIView):
    '''
    class SpecificJob
    '''
    serializer_class = PostJobSerializer

    def get_queryset(self):
        job_id = self.kwargs['pk']
        return PostJob.objects.filter(id=job_id)


class EmployerJob(generics.ListAPIView):
    '''
    class EmployerJob
    '''
    serializer_class = PostJobSerializer

    def get_queryset(self):
        employer_id = self.kwargs['employer_id']
        employer = Employer.objects.get(pk=employer_id)
        return PostJob.objects.filter(employer=employer)


class CompanyProfileDetails(generics.ListCreateAPIView):
    '''
    class CompanyProfileDetails
    '''
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
