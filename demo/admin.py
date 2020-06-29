from django.contrib import admin
from .models import File
# Register your models here.

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fields = ['filename', 'sha256', 'filesize', 'mimetype']
    list_display = ['filename', 'filesize']
    list_filter = ['filename', 'date_submitted', 'filesize']
    search_fields = ['filename','sha256','mimetype']

