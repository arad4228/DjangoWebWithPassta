from django.contrib import admin
from SMForum.forums.models import Category, Tag, ForumPost, Comment
from markdownx.admin import MarkdownxModelAdmin


# Register your models here.

# 카테고리와 태크를 기반으로 slug를 만들어준다.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(ForumPost, MarkdownxModelAdmin)
admin.site.regeister(Comment)