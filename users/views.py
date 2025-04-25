from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser

# Create your views here.
def learner(request):
    return render(request, "users/learner.html")


def teacher(request):
    return render(request, "users/teacher.html")





# Contact Page View
def contact(request):
    return render(request, "users/contact.html")


def teacher_profile(request):
    return render(request, "users/teacher_profile.html")


def learner_profile(request):
    return render(request, "users/learner_profile.html")


def parent_profile(request):
    return render(request, "users/parent_profile.html")


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
@login_required
def student_marks_view(request):
    if request.user.user_type != 'STUDENT':
        messages.error(request, "Access denied. Student access only.")
        return redirect('users:profile')
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})