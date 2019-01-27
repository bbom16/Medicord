from django import forms
from django.contrib.auth.forms import AuthenticationForm
from sign_up.models import MyUser

#로그인 폼, 필요하다면 form들을 명시해준다. (지금 해준 상태)

class LoginForm(AuthenticationForm):
    # email로 하면 field가 새로 생겨서 이름을 username으로 사용했다.
    username = forms.EmailField(
        label="",
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일',
                'required': 'True',
            }
        )
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
                'required': 'True',
            }
        )
    )

    class Meta:  # SignupForm에 대한 기술서
        model = MyUser
        fields = ("email", "password1")
