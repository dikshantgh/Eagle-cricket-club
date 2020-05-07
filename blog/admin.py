from django.contrib import admin

from blog.models import Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commented_by', 'blog', )