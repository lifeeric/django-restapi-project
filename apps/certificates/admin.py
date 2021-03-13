from django.contrib import admin
from .models import Certificate


class AdminCertificate(admin.ModelAdmin):
    list_display = ('name', 'description', 'updated_at', 'created_at')
    search_fields = ('name',)


admin.site.register(Certificate, AdminCertificate)
