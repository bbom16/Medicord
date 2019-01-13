from django.shortcuts import render
from django.utils import timezone
from .models import Diary

def diary_list(request):
    context = {}
    context['diary_list'] = Diary.objects.all().order_by('record_date')
    return render(request, 'diary.html', context)   #request : 사용자가 요청한 것, context는 넘겨주는 인자

