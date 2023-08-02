import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200) #200 길이까지 입력되는 문자열 필드
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #외래키?
    choice_text = models.CharField(max_length=200) #이것도 문자열 필드
    votes = models.IntegerField(default=0) #이건 숫자 필드
    def __str__(self):
        return self.choice_text