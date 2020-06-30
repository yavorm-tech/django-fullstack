from django.contrib import admin
from .models import File, FileMetadata, Evaluation, Client
# Register your models here.

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fields = ['filename', 'sha256', 'filesize', 'mimetype', 'metadata']
    list_display = ['filename', 'filesize']
    list_filter = ['filename', 'date_submitted', 'filesize']
    search_fields = ['filename','sha256','mimetype']

admin.site.register(FileMetadata)
admin.site.register(Evaluation)
admin.site.register(Client)


