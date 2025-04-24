from django.shortcuts import render
from .models import Course


# Courses Page View
def courses(request):
    courses = Course.objects.all()
    print(courses)
    return render(request, "courses/courses.html", {"courses": courses})


# Routine Page View
def routine(request):
    return render(request, "courses/routine.html")
