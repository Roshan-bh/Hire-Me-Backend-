'''
accounts models.py file to store the models related to the account.
'''
from django.db import models
from django.core import serializers


class Candidate(models.Model):
    '''
    To register a new candidate.
    '''
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    password = models.CharField(max_length=100, null=True)
    confirm_password = models.CharField(max_length=100, null=True)
    phone_number = models.BigIntegerField(null=True,
                                          blank=True, unique=True)
    candidate_image = models.ImageField(
        upload_to="images/candidate_images/", null=True)
    sectors = models.TextField()
    resume = models.FileField(blank=True, null=True)
    terms_condition = models.BooleanField(default=False)

    class Meta:
        '''
        Meta information for Candidate class.
        '''
        verbose_name_plural = '1. Candidates'

    def __str__(self):
        return str(self.email)


class CompanyProfile(models.Model):
    '''
    CompanyProfile class
    '''
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=250)
    email = models.EmailField()
    website = models.CharField(max_length=300, unique=True)
    sector = models.TextField()
    established_date = models.DateField()
    contact_number = models.PositiveBigIntegerField()
    company_description = models.TextField(null=True, blank=True)
    company_profile_img = models.ImageField(
        upload_to='images/company_profile/', blank=True)
    facebook_link = models.URLField(null=True, blank=True, unique=True)
    twitter_link = models.URLField(null=True, blank=True, unique=True)
    linkedin_link = models.URLField(null=True, blank=True, unique=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=100)
    exact_location = models.CharField(max_length=250)

    class Meta:
        '''
        Meta information for companyprofile class.
        '''
        verbose_name_plural = '2. CompanyProfiles'

    def __str__(self):
        return str(self.company_name)


class Employer(models.Model):
    '''
    To register a new Employer.
    '''
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    phone_number = models.BigIntegerField(
        null=True, blank=True, unique=True)
    organization_name = models.CharField(max_length=200)
    companyProfile = models.ForeignKey(
        CompanyProfile, on_delete=models.CASCADE, related_name="company_profile", null=True, blank=True)
    terms_condition = models.BooleanField(default=False)

    class Meta:
        '''
        Meta information for Employer class.
        '''
        verbose_name_plural = '3. Employers'

    def __str__(self):
        return str(self.email)


class JobSector(models.Model):
    '''
    class to define  different job sectors.
    '''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        '''
        Meta information for JobSector class.
        '''
        verbose_name_plural = '4. JobSectors'

    def __str__(self):
        return str(self.title)


class JobType(models.Model):
    '''
    class to define  different job types.
    '''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        '''
        Meta information for JobType class.
        '''
        verbose_name_plural = '5. JobTypes'

    def __str__(self):
        return str(self.title)


class SalaryType(models.Model):
    '''
    class to define  different salary types.
    '''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        '''
        Meta information for SalaryType class.
        '''
        verbose_name_plural = '6. SalaryTypes'

    def __str__(self):
        return str(self.title)


class Industry(models.Model):
    '''
    class to define  different job sectors.
    '''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        '''
        Meta information for Industry class.
        '''
        verbose_name_plural = '7. Industries'

    def __str__(self):
        return str(self.title)


class PostJob(models.Model):
    '''
    post job
    '''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    company_name = models.ForeignKey(
        CompanyProfile, on_delete=models.CASCADE, null=True, blank=True)
    employer = models.ForeignKey(
        Employer, on_delete=models.CASCADE, default="")
    description = models.TextField(blank=True, null=True)
    application_deadline = models.DateTimeField()
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    job_sector = models.ForeignKey(
        JobSector, on_delete=models.CASCADE, related_name="job_sector")
    required_skills = models.TextField()
    salary_type = models.ForeignKey(SalaryType, on_delete=models.CASCADE)
    salary_minimum = models.PositiveIntegerField()
    salary_maximum = models.PositiveIntegerField()
    job_image = models.ImageField(upload_to='images/jobs/', null=True)
    experience = models.CharField(max_length=255, default='')
    qualification = models.CharField(max_length=255, default='')
    industry = models.ForeignKey(
        Industry, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=100)
    exact_location = models.CharField(max_length=250)
    created_at = models.DateField(
        auto_now_add=True, null=True)
    terms_conditions = models.BooleanField(default=False)

    class Meta:
        '''
        Meta information for postjob class.
        '''
        verbose_name_plural = '8. PostJobs'

    def __str__(self):
        return str(self.title)

    def related_jobs(self):
        '''
        method to get related jobs.
        '''
        related_jobs = PostJob.objects.filter(
            required_skills__icontains=self.required_skills)
        return serializers.serialize('json', related_jobs)


class CandidateJobApplication(models.Model):
    '''
    CandidateJobApplication class
    '''
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(
        PostJob, on_delete=models.CASCADE, related_name="appied_jobs", default="")
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name="applied_candidates", default="")
    applied_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        mata information
        '''
        verbose_name_plural = "9. CandidateJobApplications"

    def __str__(self):
        return f"{self.job}-{self.candidate}"


class PostInternship(models.Model):
    '''
    PostInternship
    '''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    company_name = models.ForeignKey(
        CompanyProfile, on_delete=models.CASCADE, null=True)
    employer = models.ForeignKey(
        Employer, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True, null=True)
    application_deadline = models.DateTimeField()
    internship_type = models.ForeignKey(
        JobType, on_delete=models.CASCADE, null=True)
    internship_sector = models.ForeignKey(
        JobSector, on_delete=models.CASCADE, related_name="internship_sector", null=True)
    required_skills = models.TextField()
    salary_type = models.ForeignKey(
        SalaryType, on_delete=models.CASCADE, null=True)
    salary_minimum = models.PositiveIntegerField()
    salary_maximum = models.PositiveIntegerField()
    internship_image = models.ImageField(
        upload_to='images/internships/', null=True)
    experience = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    industry = models.ForeignKey(
        Industry, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=100)
    exact_location = models.CharField(max_length=250)
    created_at = models.DateField(
        auto_now_add=True)
    terms_conditions = models.BooleanField(default=False)

    class Meta:
        '''
        Meta information for PostInternship class.
        '''
        verbose_name_plural = '10. PostInternship'

    def __str__(self):
        return str(self.title)

    def related_internships(self):
        '''
        method to get related internships.
        '''
        related_internships = PostInternship.objects.filter(
            required_skills__icontains=self.required_skills)
        return serializers.serialize('json', related_internships)
