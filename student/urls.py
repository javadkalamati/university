from django.urls import path
from . import views
urlpatterns=[
    path("home/",views.home),
    path("details/<int:person_id>/",views.detail),
]