from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
  path("book/",  views.book , name="book"),
]