from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)        # 제목
    content = models.TextField()                    # 내용

    image = models.ImageField(upload_to="Forum/images/%Y/%m/%d/", blank=True)   # 사용자가 올릴 이미지

    author = models.ForeignKey(User, on_delete=models.CASCADE)                  # 글쓴이
    create_at = models.DateTimeField(auto_now_add=True)                         # 글을 생성한 시간
    update_at = models.DateTimeField(auto_now=True)                             # 글을 마지막으로 수정한 시간

    def __str__(self):
        return f'[{self.pk}] [{self.title}] :: {self.author}'