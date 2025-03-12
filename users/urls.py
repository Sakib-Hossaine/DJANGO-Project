from django.urls import path
from . import views

urlpatterns = [
    path("learner/", views.learner, name="learner"),
    path("teacher/", views.teacher, name="teacher"),
    path("parent/", views.parent, name="parent"),
    path("contact/", views.contact, name="contact"),
    path("teacher-profile/", views.teacher_profile, name="teacher_profile"),
    # Other URLs
]
