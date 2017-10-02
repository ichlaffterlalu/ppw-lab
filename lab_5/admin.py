from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
	list_display = ('created_date','title','description')
	list_display_links = ('title','description')
	search_fields = ('title','description')
	list_per_page = 50

admin.site.register(Todo,TodoAdmin)