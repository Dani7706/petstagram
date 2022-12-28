from django.contrib import admin

from petstagram_last.common.models import Comment


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text',)