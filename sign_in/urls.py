from django.urls import path
from . import views

# 새 url 등록시 medicord url에 등록 필요. 새 app 발생시에도 반드시!! medicord setting에 등록!!!
urlpatterns = [
    path('login/', views.signin, name='sign_in'),
    path('logout/', views.signout, name='sign_out'),
]
