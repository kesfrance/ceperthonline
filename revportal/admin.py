from django.contrib import admin
from revportal.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views')

admin.site.register(Post, PostAdmin)