from django.contrib import admin
from .models import PresentationEmail


@admin.register(PresentationEmail)
class PresentationEmailAdmin(admin.ModelAdmin):
    list_display = ['identification', 'email', 'is_sent', 'sent_date']
    search_fields = ['identification']
    readonly_fields = ['hash']
