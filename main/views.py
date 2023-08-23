'''
views.py
'''
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .serializers import EmployerSerializer, CandidateSerializer, JobSectorSerializer, JobTypeSerializer, SalaryTypeSerializer, PostJobSerializer, PostInternshipSerializer, IndustrySerializer, CompanyProfileSerializer, CandidateJobApplicationSerializer, CandidateInternshipApplicationSerializer
from .models import Candidate, Employer, JobType, JobSector, SalaryType, Industry, PostJob, PostInternship, CompanyProfile, CandidateJobApplication, CandidateInternshipApplication


# Create your views here.


class StandardResultsSetPagination(PageNumberPagination):
    '''
    StandardResultsSetPagination class implementation
    '''
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2


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
    pagination_class = StandardResultsSetPagination

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


class Internship(generics.ListCreateAPIView):
    '''
    class Internship
    '''
    queryset = PostInternship.objects.all()
    serializer_class = PostInternshipSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        query_set = super().get_queryset()
        if 'result' in self.request.GET:
            limit = int(self.request.GET['result'])
            query_set = PostInternship.objects.all().order_by('-id')[:limit]
        return query_set


class SpecificInternship(generics.RetrieveUpdateDestroyAPIView):
    '''
    class SpecificInternship
    '''
    serializer_class = PostInternshipSerializer

    def get_queryset(self):
        internship_id = self.kwargs['pk']
        return PostInternship.objects.filter(id=internship_id)


class EmployerJob(generics.ListAPIView):
    '''
    class EmployerJob
    '''
    serializer_class = PostJobSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        employer_id = self.kwargs['employer_id']
        employer = Employer.objects.get(pk=employer_id)
        return PostJob.objects.filter(employer=employer)


class CompanyProfileList(generics.RetrieveUpdateDestroyAPIView):
    '''
    class CompanyProfileDetails
    '''
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class CompanyProfileDetails(generics.ListCreateAPIView):
    '''
    class CompanyProfileDetails
    '''
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class CandidateInternshipApplicationList(generics.ListCreateAPIView):
    '''CandidateInternshipApplicationList class'''

    queryset = CandidateInternshipApplication.objects.all()
    serializer_class = CandidateInternshipApplicationSerializer


def fetch_apply_status_internship(request, candidate_id, internship_id):
    '''
    to check whether a candidate applied for a internship.
    '''
    candidate = Candidate.objects.filter(id=candidate_id).first()
    internship = PostInternship.objects.filter(id=internship_id).first()
    apply_status = CandidateInternshipApplication.objects.filter(
        internship=internship, candidate=candidate).count()
    if apply_status:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})


class CandidateInternshipAppliedData(generics.ListAPIView):
    '''
    class CandidateInternshipAppliedData
    '''
    queryset = CandidateInternshipApplication.objects.all()
    serializer_class = CandidateInternshipApplicationSerializer

    def get_queryset(self):
        if 'candidate_id' in self.kwargs:
            candidate_id = self.kwargs['candidate_id']
            candidate = Candidate.objects.get(pk=candidate_id)
            return CandidateInternshipApplication.objects.filter(candidate=candidate).distinct()


class CandidateInternshipAppliedDetails(generics.RetrieveUpdateDestroyAPIView):
    '''
    class CandidateInternshipAppliedDetails
    '''
    queryset = CandidateInternshipApplication.objects.all()
    serializer_class = CandidateInternshipApplicationSerializer


class CandidateJobApplicationList(generics.ListCreateAPIView):
    '''CandidateJobApplicationList class'''

    queryset = CandidateJobApplication.objects.all()
    serializer_class = CandidateJobApplicationSerializer


def fetch_apply_status_job(request, user_id, job_id):
    '''
    to check whether a candidate applied for a job.
    '''
    candidate = Candidate.objects.filter(id=user_id).first()
    job = PostJob.objects.filter(id=job_id).first()
    apply_status = CandidateJobApplication.objects.filter(
        job=job, candidate=candidate).count()
    if apply_status:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})


class CandidateJobAppliedData(generics.ListAPIView):
    '''
    class CandidateJobAppliedData
    '''
    queryset = CandidateJobApplication.objects.all()
    serializer_class = CandidateJobApplicationSerializer

    def get_queryset(self):
        if 'candidate_id' in self.kwargs:
            candidate_id = self.kwargs['candidate_id']
            candidate = Candidate.objects.get(pk=candidate_id)
            return CandidateJobApplication.objects.filter(candidate=candidate).distinct()


class CandidateJobAppliedDetails(generics.RetrieveUpdateDestroyAPIView):
    '''
    class CandidateJobAppliedData
    '''
    queryset = CandidateJobApplication.objects.all()
    serializer_class = CandidateJobApplicationSerializer


@csrf_exempt
def employer_change_password(request, employer_id):
    '''
    change Password for specific employer
    '''
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    try:
        employer_data = Employer.objects.get(id=employer_id)
    except Employer.DoesNotExist:
        employer_data = None
    if employer_data:
        Employer.objects.filter(id=employer_id).update(
            password=password, confirm_password=confirm_password)
        return JsonResponse({'bool': True, 'employer_id': employer_data.id})
    if employer_data is None:
        return JsonResponse({'bool': False})


@csrf_exempt
def candidate_change_password(request, candidate_id):
    '''
    change Password for specific candidate
    '''
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    try:
        candidate_data = Candidate.objects.get(id=candidate_id)
    except Candidate.DoesNotExist:
        candidate_data = None
    if candidate_data:
        Candidate.objects.filter(id=candidate_id).update(
            password=password, confirm_password=confirm_password)
        return JsonResponse({'bool': True})
    if candidate_data is None:
        return JsonResponse({'bool': False})
