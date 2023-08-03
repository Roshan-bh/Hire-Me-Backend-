'''
views.py
'''
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployerSerializer, CandidateSerializer
from .models import Candidate, Employer

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
