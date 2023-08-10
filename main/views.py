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
from .serializers import EmployerSerializer, CandidateSerializer, JobSectorSerializer, JobTypeSerializer, SalaryTypeSerializer
from .models import Candidate, Employer, JobType, JobSector, SalaryType

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
def user_login(request):
    '''
    login credentials check funciton
    '''
    email = request.POST.get('email')
    password = request.POST.get('password')
    employer_data = get_object_or_404(Employer, email=email, password=password)
    # candidate_data = Candidate.objects.get(
    #     email=email, password=password)
    if employer_data:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})
    # if candidate_data:
    #     return JsonResponse({'bool': True})
    # else:
    #     return JsonResponse({'bool': False})


class JobSectorList(generics.ListCreateAPIView):
    '''
    class JobSectorList
    '''
    queryset = JobSector.objects.all()
    serializer_class = JobSectorSerializer


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
    queryset = JobType.objects.all()
    serializer_class = SalaryTypeSerializer
