from django.db import models

class Company(models.Model):
    ENTITY_CHOICES = [
        ('COMPANY', 'Company'),
        ('STARTUP', 'Startup'),
        ('FREELANCER', 'Freelancer'),
        ('AGENCY', 'Agency / Consultant'),
    ]

    name = models.CharField(max_length=200)
    entity_type = models.CharField(
        max_length=20,
        choices=ENTITY_CHOICES,
        default='COMPANY'
    )
    industry = models.CharField(max_length=100, blank=True)
    size_range = models.CharField(max_length=50, blank=True)  # e.g. "1-10", "10-50"

    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True)

    seats_required = models.IntegerField()

    SPACE_CHOICES = [
        ('OPEN', 'Open Desk'),
        ('DEDICATED', 'Dedicated Desk'),
        ('CABIN', 'Private Cabin'),
        ('MEETING', 'Meeting Room Only'),
    ]
    space_type = models.CharField(max_length=20, choices=SPACE_CHOICES)

    start_date = models.DateField(null=True, blank=True)
    duration_months = models.IntegerField(null=True, blank=True)
    budget_per_seat = models.IntegerField(null=True, blank=True)

    amenities = models.TextField(blank=True)
    description = models.TextField(blank=True)

    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('IN_REVIEW', 'In Review'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('ON_HOLD', 'On Hold'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NEW'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
