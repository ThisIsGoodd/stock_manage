from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question') #글쓴이
    subject = models.CharField(max_length=200) #제목
    content = models.TextField() #내용
    create_date = models.DateTimeField() #작성 날짜
    modify_date = models.DateTimeField(null=True, blank=True) #수정 날짜
    voter = models.ManyToManyField(User, related_name='voter_question') # 추천인
    
    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer') #글쓴이
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #글
    content = models.TextField() #내용
    create_date = models.DateTimeField()  #작성 날짜
    modify_date = models.DateTimeField(null=True, blank=True) #수정 날짜
    voter = models.ManyToManyField(User, related_name='voter_answer') # 추천인