from django.contrib import admin

# Register your models here.
from .models import Post
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Post)