from django.contrib import admin
from .models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'meal', 'profile']

admin.site.register(Comment, CommentAdmin)
