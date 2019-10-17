from django.urls import path
from checkin import views

urlpatterns = [
  path("", views.home, name="home"),
  path("greet/<name>", views.greet, name="greet"),
]