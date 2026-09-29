# Create your models here.
import uuid

from django.contrib.auth.models import User
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    thumbnail_url = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(blank=True, null=True)
    starred_by = models.ManyToManyField(
        User, related_name="starred_experience", blank=True
    )
    
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None
    
    @property
    def thumbnail_display(self):
        if self.thumbnail:
            return self.thumbnail
        if self.thumbnail_url:
            return self.thumbnail_url
        return None
            
    
#Tugas Individu 2
class Education(models.Model):
    EDUCATION_CHOICES = [
        ('SD', 'Sekolah Dasar'),
        ('SMP', 'Sekolah Menengah Pertama'),
        ('SMA', 'Sekolah Menengah Atas'),
        ('S1', 'Program Sarjana')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    thumbnail_url = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.institution
        
    @property
    def is_ongoing(self):
        return self.ended_at is None
    
    @property
    def thumbnail_display(self):
        if self.thumbnail:
            return self.thumbnail
        if self.thumbnail_url:
            return self.thumbnail_url
        return None
    
#Tugas Individu 3
class Contact(models.Model):
    CONTACT_CHOICES = [
        ('email', 'Email'),
        ('instagram', 'Instagram'),
        ('linkedin', 'Linkedin'),
        ('whatsapp', 'Whatsapp'),
        ('line', 'Line'),
        ('github', 'Github'),
        ('others', 'Lainnya'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CONTACT_CHOICES)
    value = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    
    def __str__(self):
            return self.name
        
#Tugas Individu 3
class Project(models.Model):
    ROLE_CHOICES = [
            ('PM', 'Product Manager'),
            ('PM', 'Project Manager'),
            ('PS', 'Project Support'),
            ('Dev', 'Web Developer'),
            ('Des', 'Designer'),
        ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(User, related_name="starred_project", blank=True)

    def __str__(self):
        return self.title
    
class Design(models.Model):
    CATEGORY_CHOICES = [
        ('Personal', 'Personal Project'),
        ('Group', 'Group Project'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    tools = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(User, related_name="starred_design", blank=True)
        
#Tugas Individu 4
class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=100, blank=True, null=True)
    to = models.CharField(max_length=100, blank=True, null=True)
    value = models.TextField()
    starred_by = models.ManyToManyField(
        User, related_name="starred_message", blank=True
    )
    
    def __str__(self):
            return self.value