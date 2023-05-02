from django.contrib import admin
from .models import Post, Comment


class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_by')


class AdminComment(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_by', 'in_post')
# Register your models here.


admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)
