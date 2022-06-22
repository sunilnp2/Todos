from django.contrib import admin
from list.models import *
# Register your models here.
class Todo(admin.ModelAdmin):
    list_display = ['username', 'title', 'slug']


admin.site.register(Todo_List)