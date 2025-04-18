from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("courses/", views.courses, name="courses"),
    path("notes/", views.notes, name="notes"),
    path("routine/", views.routine, name="routine"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)