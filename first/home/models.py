from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    established_year = models.IntegerField(default=1900)
    is_public = models.BooleanField(default=True)
    ranking = models.IntegerField(null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "01. Universities"
    
    def __str__(self):
        return self.name

class Department(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    head_of_department = models.CharField(max_length=255, null=True, blank=True)
    established_year = models.IntegerField(default=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "02. Departments"
        
    def __str__(self):
        return f"{self.name} - {self.university.name}"