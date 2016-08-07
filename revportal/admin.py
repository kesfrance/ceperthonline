from django.contrib import admin
from revportal.models import Post, UserProfile



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views')
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'picture')

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, ProfileAdmin)