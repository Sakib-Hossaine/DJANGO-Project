from django.shortcuts import render

# Courses Page View
def courses(request):
    return render(request, 'courses/courses.html')

# Notes Page View
def notes(request):
    return render(request, 'courses/notes.html')

# Routine Page View
def routine(request):
    return render(request, 'courses/routine.html')

