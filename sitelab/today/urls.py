from django.urls import path
from . import views

app_name = "today"

urlpatterns = [
    path("today/", views.today, name="today"),
]