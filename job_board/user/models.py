from django.db import models
from django.contrib.auth.models import User
 
class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, null=True,)
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    about = models.TextField(null=True, blank=True)
    work = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    cv = models.FileField(upload_to="resumes/", null=True, blank=True)
    district= models.TextField(null=True, blank=True)
    state= models.TextField(null=True, blank=True)
    country= models.TextField(null=True, blank=True)
    pincode= models.TextField(null=True, blank=True)
    EDUCATION_CHOICES = [
        ('diploma', 'Diploma'),
        ('graduate', 'Graduate'),
        ('post_graduate', 'Post Graduate'),
        ('iti', 'ITI'),
    ]

    education_level = models.CharField(max_length=20, choices=EDUCATION_CHOICES, default='graduate')

 
    def __str__(self):
        return self.user.first_name
 
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="companies/", null=True, blank=True)   
    type = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    company_name = models.CharField(max_length=100)
    website = models.TextField(null=True, blank=True)
 
    def __str__ (self):
        return self.user.username
    
    def vacancy_count(self):
        return self.job_set.count() 
 
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=200)
    salary = models.FloatField()
    image = models.ImageField(upload_to="jobs/", null=True, blank=True)
    description = models.TextField(max_length=400)
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    creation_date = models.DateField() 
    featured = models.BooleanField(default=False)  
 
    FULL_TIME = 'full'
    PART_TIME = 'part'
    BOTH = 'both'
    JOB_TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (BOTH, 'Both (Full-Time and Part-Time)'),
    ]
 
    OFFICE = 'office'
    HOME = 'home'
    FIELD = 'field'
    WORK_LOCATION_CHOICES = [
        (OFFICE, 'Work from office'),
        (HOME, 'Work from home'),
        (FIELD, 'Field job'),
    ]

    title = models.CharField(max_length=255)
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES, default=FULL_TIME)
    work_location = models.CharField(max_length=10, choices=WORK_LOCATION_CHOICES, default=OFFICE)
  
 
    def __str__ (self):
        return self.title
 
class Application(models.Model):
    company = models.CharField(max_length=200, default="")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    resume = models.ImageField(upload_to="resumes/")
    apply_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
 
    def __str__ (self):
        return str(self.applicant)
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}"