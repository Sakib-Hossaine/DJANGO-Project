from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(upload_to='teacher_profiles/', null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    qualification = models.CharField(max_length=100)
    subjects_taught = models.CharField(max_length=200)
    zoom_link = models.URLField(max_length=300)
    
    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(upload_to='student_profiles/', null=True, blank=True)
    class_name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=100)
    address = models.TextField()
    parent_phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username

class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=100)
    math_score = models.DecimalField(max_digits=5, decimal_places=2)
    science_score = models.DecimalField(max_digits=5, decimal_places=2)
    english_score = models.DecimalField(max_digits=5, decimal_places=2)
    total_score = models.DecimalField(max_digits=5, decimal_places=2)
    date_taken = models.DateField()
    
    def save(self, *args, **kwargs):
        self.total_score = self.math_score + self.science_score + self.english_score
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.student.user.username} - {self.exam_name}"