from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from sign_in.views import signin, LoginForm
from .models import Diary

def diary_list(request):
    context = {}
    usr = request.user
    # 자신이 작성한 글만 보이기
    if request.user.is_authenticated:
        context['usr'] = usr
        context['diary_list'] = Diary.objects.filter(author=usr).order_by('record_date')
    else:
        return signin(request)
    return render(request, 'diary.html', context)   #request : 사용자가 요청한 것, context는 넘겨주는 인자

def diary_detail(request, pk):
    context = {}
    context['diary'] = get_object_or_404(Diary, pk=pk)
    return render(request, 'diary_detail.html', context)

def diary_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.author = request.user
            diary.save()
            return redirect('diary_detail', pk=diary.pk)
    else:
        form = PostForm()

    return render(request, 'diary_edit.html', {'form': form})

def diary_edit(request, pk):
    post = get_object_or_404(Diary, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.author = request.user
            diary.published_time = timezone.now()
            post.save()
            return redirect('diary_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'diary_edit.html', {'form': form})