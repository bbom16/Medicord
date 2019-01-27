from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout

#로그인 기능 구현. 로그인 되면 메인페이지로, 실패하면 실패 문구. 로그아웃 기능 필요
def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('diary')
        else:
            return HttpResponse('로그인 실패, 아이디와 비밀번호를 확인해주세요.')
    else:
        form = LoginForm()
        return render(request, 'sign_in.html', {'form': form})

# def signin(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username = username, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect('diary')
#         else:
#             return HttpResponse('로그인 실패. 다시 시도 해보세요.')
#     else:
#         form = LoginForm()
#         return render(request, 'sign_in.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('diary')



