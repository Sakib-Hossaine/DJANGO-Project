from django.shortcuts import render


# Create your views here.
def learner(request):
    return render(request, "users/learner.html")


def teacher(request):
    return render(request, "users/teacher.html")


def parent(request):
    return render(request, "users/parent.html")


# Contact Page View
def contact(request):
    return render(request, "users/contact.html")


def teacher_profile(request):
    return render(request, "users/teacher_profile.html")


def learner_profile(request):
    return render(request, "users/learner_profile.html")


def parent_profile(request):
    return render(request, "users/parent_profile.html")
