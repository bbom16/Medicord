from django.db import models
from django.utils import timezone

class Diary(models.Model):
    record_date = models.DateField(default=timezone.now)    #날짜
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   #작성자
    meal_time = models.TimeField()  #식사 시간
    meal_type = models.CharField(max_length=3)  #식사 종류(아침, 점심, 저녁, 간식 중)
    meal_contents = models.CharField(max_length=200)      #식사 음식
    medicine_time = models.TimeField()      #약 복용 시간
    medicine_contents = models.CharField(max_length=200)    #약 종류
    pain = models.CharField(max_length=300)     #통증
    pain_degree = models.IntegerField()         #통증 세기
    condition = models.TextField()    #전반적인 컨디션 정보
    published_time = models.DateTimeField(default=timezone.now) #저장 날짜, 수정시 업데이트

    def recording(self):
        self.save()

    def __str__(self):
        return str(self.record_date) #datafield를 return 하려면 str함수 사용
