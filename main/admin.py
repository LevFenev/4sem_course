from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin

class RecordsExcel(ImportExportActionModelAdmin):
    pass

admin.site.register(Post, RecordsExcel)

admin.site.register(Type, RecordsExcel)