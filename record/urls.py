from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.diary_list, name='diary'),
    path('diary/detail/<int:pk>', views.diary_detail, name='diary_detail'),
    path('diary/new/', views.diary_new, name='diary_new'),
    path('diary/new/<int:pk>', views.diary_edit, name="diary_edit"),

]