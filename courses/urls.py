from django.urls import path
from . import views 

urlpatterns = [
    path("courses/", views.courses, name="courses"),
    path("notes/", views.notes, name="notes"),
    path("routine/", views.routine, name="routine"),
]