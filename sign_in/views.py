from django.shortcuts import render, redirect
from django.http import HttpResponse
from sign_up.forms import UserForm
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext

# Create your views here.

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect('diary')
        else:
            return HttpResponse('로그인 실패, 아이디와 비밀번호를 확인해주세요.')
    else:
        form = LoginForm()
        return render(request, 'sign_in.html', {'form':form})



