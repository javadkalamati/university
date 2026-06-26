from django.urls import path
from . import views
urlpatterns=[
    path("home/",views.home,name='Home'),
    path("details/<int:person_id>/",views.detail,name='details'),
    path('delete/<int:person_id>/',views.delete,name='delete'),
    path('update/<int:person_id>/',views.update,name='update'),
    path('create/',views.create,name='create'),
]