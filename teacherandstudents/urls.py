from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.profile, name='profile'),
    path('profiles/marks/', views.student_marks, name='student_marks'),
]