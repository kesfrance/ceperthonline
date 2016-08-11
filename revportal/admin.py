from django.contrib import admin
from revportal.models import Post, UserProfile, Review



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views')
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'picture')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('content', 'created', 'author', 'post')
    
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Review, ReviewAdmin)