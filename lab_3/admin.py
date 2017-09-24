from django.contrib import admin
from .models import Diary

# Register your models here.
class DiaryAdmin(admin.ModelAdmin):
	list_display = ('activity','date')
	list_display_links = ('activity',)
	search_fields = ('activity',)
	list_per_page = 50

admin.site.register(Diary, DiaryAdmin)