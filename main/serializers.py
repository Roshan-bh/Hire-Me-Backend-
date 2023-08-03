'''
accounts serializers.py file.
'''
from rest_framework import serializers
from .models import Candidate, Employer


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
    #     extra_kwargs = {'password': {'write_only': True},
    #                     'confirm_password': {'write_only': True}}

    # def validate(self, attrs):
    #     password = attrs.get('password')
    #     confirm_password = attrs.get('confirm_password')
    #     if password != confirm_password:
    #         raise serializers.ValidationError(
    #             "Password and Confirm Password must be the same.")
    #     return attrs
