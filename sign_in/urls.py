from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signin, name='sign_in'),
]