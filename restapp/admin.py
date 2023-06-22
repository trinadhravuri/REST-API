from django.contrib import admin
from .models import UserProfile,ProfileFeedItem
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['name','email']

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(ProfileFeedItem)