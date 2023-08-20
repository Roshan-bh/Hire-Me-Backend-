'''
accounts serializers.py file.
'''
from rest_framework import serializers
from .models import Candidate, Employer, JobSector, JobType, SalaryType, PostJob, PostInternship, Industry, CompanyProfile, CandidateJobApplication, CandidateInternshipApplication


class CandidateSerializer(serializers.ModelSerializer):
    '''
    candidate serializer to serialize a candidate data.
    '''
    class Meta:
        '''
        meta information.
        '''
        model = Candidate
        fields = '__all__'
        depth = 1


class EmployerSerializer(serializers.ModelSerializer):
    '''
    employer serializer to serialize a employer data.
    '''
    class Meta:
        '''
        meta information.
        '''
        model = Employer
        fields = '__all__'
        depth = 1
    #     extra_kwargs = {'password': {'write_only': True},
    #                     'confirm_password': {'write_only': True}}

    # def validate(self, attrs):
    #     password = attrs.get('password')
    #     confirm_password = attrs.get('confirm_password')
    #     if password != confirm_password:
    #         raise serializers.ValidationError(
    #             "Password and Confirm Password must be the same.")
    #     return attrs


class JobSectorSerializer(serializers.ModelSerializer):
    '''
    serializer for JobSector
    '''
    class Meta:
        '''
        meta information
        '''
        model = JobSector
        fields = '__all__'


class JobTypeSerializer(serializers.ModelSerializer):
    '''
    serializer for JobType
    '''
    class Meta:
        '''
        meta information
        '''
        model = JobType
        fields = '__all__'


class SalaryTypeSerializer(serializers.ModelSerializer):
    '''
    serializer for JobType
    '''
    class Meta:
        '''
        meta information
        '''
        model = SalaryType
        fields = '__all__'


class IndustrySerializer(serializers.ModelSerializer):
    '''
    serializer for JobSector
    '''
    class Meta:
        '''
        meta information
        '''
        model = Industry
        fields = '__all__'


class PostJobSerializer(serializers.ModelSerializer):
    '''
    serializer for PostJob
    '''
    class Meta:
        '''
        meta information
        '''
        model = PostJob
        # fields = '__all__'
        # extra_fields = ['related_jobs']
        fields = ['id', 'title', 'employer', 'description', 'application_deadline', 'job_type', 'job_sector',
                  'required_skills', 'salary_type', 'salary_minimum', 'salary_maximum', 'job_image', 'experience', 'qualification', 'industry', 'country', 'city', 'postal_code', 'exact_location', 'created_at', 'terms_conditions',  'related_jobs']
        depth = 2


class PostInternshipSerializer(serializers.ModelSerializer):
    '''
    serializer for PostInternship
    '''
    class Meta:
        '''
        meta information
        '''
        model = PostInternship
        # fields = '__all__'
        # extra_fields = ['related_jobs']
        fields = ['id', 'title', 'employer', 'description', 'application_deadline', 'internship_type', 'internship_sector',
                  'required_skills', 'salary_type', 'salary_minimum', 'salary_maximum', 'internship_image', 'experience', 'qualification', 'industry', 'country', 'city', 'postal_code', 'exact_location', 'created_at', 'terms_conditions',  'related_internships']
        depth = 2


class CompanyProfileSerializer(serializers.ModelSerializer):
    '''
    srializer for CompanyProfile
    '''
    class Meta:
        '''
        meta information
        '''
        model = CompanyProfile
        fields = '__all__'
        depth = 2


class CandidateJobApplicationSerializer(serializers.ModelSerializer):
    '''
    srializer for CandidateJobApplication
    '''
    class Meta:
        '''
        meta information
        '''
        model = CandidateJobApplication
        fields = '__all__'
        depth = 2


class CandidateInternshipApplicationSerializer(serializers.ModelSerializer):
    '''
    srializer for CandidateInternshipApplication
    '''
    class Meta:
        '''
        meta information
        '''
        model = CandidateInternshipApplication
        fields = '__all__'
        depth = 2
