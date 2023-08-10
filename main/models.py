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


class JobSector(models.Model):
    '''
    class to define  different job sectors.
    '''
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        '''
        Meta information for JobSector class.
        '''
        verbose_name_plural = '3. JobSectors'

    def __str__(self):
        return str(self.title)


class JobType(models.Model):
    '''
    class to define  different job types.
    '''
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        '''
        Meta information for JobType class.
        '''
        verbose_name_plural = '4. JobTypes'

    def __str__(self):
        return str(self.title)


class SalaryType(models.Model):
    '''
    class to define  different salary types.
    '''
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        '''
        Meta information for SalaryType class.
        '''
        verbose_name_plural = '5. SalaryTypes'

    def __str__(self):
        return str(self.title)


class PostJob(models.Model):
    '''
    post job
    '''
    title = models.CharField(max_length=250)
    employer = models.ForeignKey(
        Employer, on_delete=models.CASCADE, default="")
    description = models.TextField(blank=True, null=True)
    application_deadline = models.DateTimeField()
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    required_skills = models.TextField()
    salary_type = models.ForeignKey(SalaryType, on_delete=models.CASCADE)
    salary_minimun = models.PositiveIntegerField()
    salary_maximun = models.PositiveIntegerField()
    job_image = models.ImageField(upload_to='images/jobs/')
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=100)
    exact_location = models.CharField(max_length=250)
    terms_conditions = models.BooleanField(default=False)

    class Meta:
        '''
        Meta information for postjob class.
        '''
        verbose_name_plural = '6. PostJobs'

    def __str__(self):
        return str(self.title)


class CompanyProfile(models.Model):
    '''
    CompanyProfile class
    '''
    company_name = models.CharField(max_length=250)
    email = models.EmailField()
    website = models.CharField(max_length=300, unique=True)
    sector = models.TextField()
    established_date = models.DateField()
    contact_number = models.PositiveBigIntegerField()
    company_profile_img = models.ImageField(
        upload_to='images/company_profile/')
    facebook_link = models.URLField(null=True, blank=True, unique=True)
    Twitter_link = models.URLField(null=True, blank=True, unique=True)
    Linkedin_link = models.URLField(null=True, blank=True, unique=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=100)
    exact_location = models.CharField(max_length=250)

    class Meta:
        '''
        Meta information for companyprofile class.
        '''
        verbose_name_plural = '7. CompanyProfiles'

    def __str__(self):
        return str(self.company_name)
