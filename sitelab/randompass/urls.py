from django.urls import path
from . import views

app_name = "randompass"

urlpatterns = [
  path("randompass/",  views.randompass , name="pass"),
]