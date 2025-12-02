from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'seats_required', 'budget_per_seat', 'status', 'created_at')
    list_filter = ('status', 'space_type', 'industry')
    search_fields = ('name', 'contact_email', 'contact_name')
