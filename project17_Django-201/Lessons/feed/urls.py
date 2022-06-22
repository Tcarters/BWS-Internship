from github3 import followed_by

from django.urls import path

from . import views

app_name = "feed"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index")
]