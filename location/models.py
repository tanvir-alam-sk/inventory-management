from django.db import models
from django.utils.timezone import now

# Create your models here.
class Location(models.Model):
    id = models.CharField(
        max_length=20,
        primary_key=True
    )
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    # center = models.PointField(
    #     geography=True,
    #     null=True,
    #     blank=True
    # )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )
    location_type = models.CharField(
        max_length=20,
        choices=[
            ('continent', 'Continent'),
            ('country', 'Country'),
            ('state', 'State'),
            ('city', 'City'),
        ],
        null=False,
        blank=False
    )
    country_code = models.CharField(
        max_length=2,
        null=True,
        blank=True
    )
    state_abbr = models.CharField(
        max_length=3,
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.title} ({self.location_type})"
