from django.contrib import admin
from .models import Friend

# Register your models here.
class FriendAdmin(admin.ModelAdmin):
    list_display = ('npm','friend_name','added_at')
    list_display_links = ('npm','friend_name')
    search_fields = ('npm','friend_name')
    list_per_page = 50

admin.site.register(Friend,FriendAdmin)