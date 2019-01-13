from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.diary_list),
]