from django.contrib import admin as _admin

from .models import List as _List


class ListAdmin(_admin.ModelAdmin):
    list_display = ("name", "user", "is_completed")


_admin.site.register(_List, ListAdmin)
