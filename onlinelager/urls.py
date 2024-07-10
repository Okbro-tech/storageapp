from django.urls import path
from . import views

urlpatterns = [
    path('onlinelager/', views.members, name='onlinelager'),
]
