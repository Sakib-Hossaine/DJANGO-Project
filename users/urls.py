from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path("learner/", views.learner, name="learner"),
    path("teacher/", views.teacher, name="teacher"),
    path("contact/", views.contact, name="contact"),
  
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
   
     path('student-profile/', views.student_profile, name='student_profile'),
    path('teacher-profile/', views.teacher_profile, name='teacher_profile'),
    path('student-marks/', views.student_marks, name='student_marks'),
    # Other URLs
]
