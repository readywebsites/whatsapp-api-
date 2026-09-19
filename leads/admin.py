from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone_number", "business_category", "created_at")
    search_fields = ("full_name", "phone_number", "business_category")
    list_filter = ("primary_goal", "budget_range", "urgency", "created_at")
