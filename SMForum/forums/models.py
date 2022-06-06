# Create your models here.
import os.path

from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField
from markdown import markdown


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/forums/tag/{self.slug}/'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return f'/forums/category/{self.slug}/'


class ForumPost(models.Model):
    title = models.CharField(max_length=30)             # 제목
    hook_msg = models.TextField(blank=True)             # Hook 메시지
    content = MarkdownxField()                          # 내용

    content_image = models.ImageField(upload_to='forums/images/%Y/%m/%d/', blank=True)
    attached_file = models.FileField(upload_to='forums/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Forum의 글은 User와 one to many로 연결된다.
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자가 사라지면 글은 의미가 없어지므로 삭제

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]  [{self.title}] :: {self.author}'

    def get_absolute_url(self):
        return f'/forums/post/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.attached_file.name)

    def get_content_markdown(self):
        return markdown(self.content)


class Comment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
