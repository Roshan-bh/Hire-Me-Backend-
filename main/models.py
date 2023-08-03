'''
accounts models.py file to store the models related to the account.
'''
from django.db import models


class Candidate(models.Model):
    '''
    To register a new candidate.
    '''
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    phone_number = models.BigIntegerField(null=True, blank=True, unique=True)
    sectors = models.TextField()
    resume = models.FileField(blank=True)
    terms_condition = models.BooleanField(default=False)

    class Meta:
        '''
        Meta information for Candidate class.
        '''
        verbose_name_plural = '1. Candidates'


class Employer(models.Model):
    '''
    To register a new Employer.
    '''
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    phone_number = models.BigIntegerField(
        null=True, blank=True, unique=True)
    organization_name = models.CharField(max_length=250)
    terms_condition = models.BooleanField(default=False)

    class Meta:
        '''
        Meta information for Employer class.
        '''
        verbose_name_plural = '2. Employers'

    def __str__(self):
        return str(self.email)
