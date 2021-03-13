from django.contrib import admin
from .models import WaitlistEntry


class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'created_at', 'updated_at',)
    search_field = ('first_name', 'last_name', 'email')


admin.site.register(WaitlistEntry, WaitlistEntryAdmin)
