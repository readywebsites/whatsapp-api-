from django.db import models

class Lead(models.Model):
    phone_number = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255, blank=True)
    business_category = models.CharField(max_length=255, blank=True)
    service_area = models.CharField(max_length=100, blank=True)
    business_maturity = models.CharField(max_length=100, blank=True)
    offering_type = models.CharField(max_length=100, blank=True)
    ticket_size = models.CharField(max_length=100, blank=True)
    primary_goal = models.CharField(max_length=100, blank=True)
    acquisition_channel = models.CharField(max_length=100, blank=True)
    existing_assets = models.JSONField(default=list, blank=True)
    current_problem = models.CharField(max_length=100, blank=True)
    ad_experience = models.CharField(max_length=100, blank=True)
    budget_range = models.CharField(max_length=100, blank=True)
    urgency = models.CharField(max_length=100, blank=True)

    lead_score_intent = models.PositiveIntegerField(default=0)
    lead_score_budget = models.PositiveIntegerField(default=0)
    lead_score_urgency = models.PositiveIntegerField(default=0)
    lead_score_service_fit = models.PositiveIntegerField(default=0)

    recommended_primary = models.CharField(max_length=255, blank=True)
    recommended_secondary = models.CharField(max_length=255, blank=True)
    consultant_rationale = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name or 'Lead'} - {self.phone_number}"
