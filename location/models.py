from django.db import models
from django.utils.timezone import now
# from django.contrib.postgres.fields import JSONField, ArrayField
# from django.contrib.gis.db import models as gis_models
# from django.contrib.auth.models import User


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


# class Property(models.Model):
#     id = models.CharField(
#         max_length=20, 
#         primary_key=True
#     )
#     feed = models.PositiveSmallIntegerField(
#         default=0
#     )  # Unsigned small integer
#     title = models.CharField(
#         max_length=100
#     )
#     country_code = models.CharField(
#         max_length=2
#     )
#     bedroom_count = models.PositiveIntegerField()  # Unsigned integer
#     review_score = models.DecimalField(
#         max_digits=3, 
#         decimal_places=1, 
#         default=0.0
#     )  # Score with 1 decimal
#     usd_rate = models.DecimalField(
#         max_digits=10, 
#         decimal_places=2
#     )# Price in USD
#     center = gis_models.PointField(
#         geography=True, 
#         null=True, 
#         blank=True
#     )  # Geolocation
#     images = ArrayField(
#         models.URLField(max_length=300), 
#         blank=True, 
#         default=list
#     )  # Array of image URLs
#     location = models.ForeignKey(
#         Location, 
#         on_delete=models.CASCADE
#     )  # Foreign key to Location
#     amenities = JSONField(
#         blank=True, 
#         default=list
#     )  # JSONB array for amenities
#     user = models.ForeignKey(
#         User, 
#         on_delete=models.SET_NULL, 
#         null=True, 
#         blank=True
#     )  # FK to auth_user
#     published = models.BooleanField(
#         default=False
#     )  # Published status
#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )  # Timestamp on create
#     updated_at = models.DateTimeField(
#         auto_now=True
#     )  # Timestamp on update

#     def __str__(self):
#         return self.title


# class LocalizeAccommodation(models.Model):

#     id = models.AutoField(
#         primary_key=True
#     )
#     title = models.CharField(
#         max_length=100, 
#         help_text="Name of the accommodation"
#     )
#     feed = models.PositiveSmallIntegerField(
#         default=0, 
#         help_text="Feed number"
#     )  # Unsigned small integer
#     country_code = models.CharField(
#         max_length=2, 
#         help_text="ISO country code"
#     )  # ISO country code
#     bedroom_count = models.PositiveIntegerField(
#         help_text="Number of bedrooms"
#     )  # Unsigned integer
#     review_score = models.DecimalField(
#         max_digits=3, 
#         decimal_places=1, 
#         default=0.0, 
#         help_text="Review score"
#     )  # Score with 1 decimal
#     usd_rate = models.DecimalField(
#         max_digits=10, 
#         decimal_places=2, 
#         help_text="Price in USD"
#         )  # Price in USD
#     center = gis_models.PointField(
#         geography=True, 
#         null=True, 
#         blank=True, 
#         help_text="Geolocation (latitude and longitude)")  # Geolocation
#     images = ArrayField(
#         models.URLField(max_length=300), 
#         blank=True, 
#         default=list, 
#         help_text="Array of image URLs"
#     )  # Array of image URLs

#     amenities = JSONField(
#         blank=True, 
#         default=list, 
#         help_text="JSONB array of amenities"
#     )  # JSONB array for amenities
#     policy = JSONField(
#         blank=True, 
#         default=dict, 
#         help_text="JSONB dictionary for policies"
#     )  # JSONB dictionary for policies

#     language = models.CharField(
#         max_length=2, 
#         help_text="Language code (ISO 639-1)"
#     )  # Language code (ISO 639-1)
#     description = models.TextField(
#         help_text="Localized description"
#     )  # Localized description

#     user = models.ForeignKey(
#         User, 
#         on_delete=models.SET_NULL, 
#         null=True, 
#         blank=True, 
#         help_text="Foreign key to Django's auth_user"
#     )  # FK to auth_user
#     published = models.BooleanField(
#         default=False, 
#         help_text="Published status"
#     )  # Published status

#     created_at = models.DateTimeField(
#         auto_now_add=True, 
#         help_text="Timestamp when created"
#     )  # Timestamp on create
#     updated_at = models.DateTimeField(
#         auto_now=True, 
#         help_text="Timestamp when updated"
#     )  # Timestamp on update


#     class Meta:
#         unique_together = ("title", "language")  # One localization per title per language

#     def __str__(self):
#         return f"{self.title} - {self.language}"
