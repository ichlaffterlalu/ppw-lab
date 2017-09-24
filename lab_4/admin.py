from django.contrib import admin
from .models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
	list_display = ('created_date','name','email','message')
	list_display_links = ('message',)
	search_fields = ('name','email')
	list_per_page = 50

admin.site.register(Message,MessageAdmin)