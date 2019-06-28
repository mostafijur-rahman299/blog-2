from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'is_draft', 'title')
	list_editable = ['is_draft', 'title']

admin.site.register(Post, PostAdmin)
