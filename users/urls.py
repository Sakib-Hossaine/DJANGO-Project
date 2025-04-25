from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path("learner/", views.learner, name="learner"),
    path("teacher/", views.teacher, name="teacher"),
   
    path("contact/", views.contact, name="contact"),
    path("teacher-profile/", views.teacher_profile, name="teacher_profile"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
