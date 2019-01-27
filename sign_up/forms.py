from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.images import get_image_dimensions

from .models import MyUser


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'required': 'True',
        }
    ))
    nickname = forms.RegexField(label="닉네임", max_length=30,
                                regex=r'^[\w]+$',
                                error_messages={
                                    'invalid': "30자 이하, 특수문자는 허용되지않습니다."},
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '30자 이하, 특수문자는 허용되지않습니다.',
                                    'required': 'true',
                                }))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호를 한번 더 입력해주세요.',
                'required': 'True',
            }
        )
    )

    class Meta:  # SignupForm에 대한 기술서
        model = MyUser
        fields = ("email", "nickname", "password1", "password2",)  # 작성한 필드만큼 화면에 보여짐

