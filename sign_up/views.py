from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignupForm

# 회원 가입 기능 구현.
def signup(request):
    signupform = SignupForm()
    if request.method == "POST":
        signupform = SignupForm(request.POST, request.FILES)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            #user.avatar = signupform.cleaned_avatar()
            user.save()

            return HttpResponseRedirect(
                reverse("diary")
            )
    return render(request, "sign_up.html", {"form": signupform})

