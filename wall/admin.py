from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import WallImage, Catlog, HomePage


@admin.register(HomePage,)
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(WallImage,)
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(Catlog,)
class ViewAdmin(ImportExportModelAdmin):
    pass
