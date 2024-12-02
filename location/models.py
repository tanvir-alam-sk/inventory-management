from django.db import models
from django.contrib.gis.db import models as geomodels  # For spatial fields
from django.contrib.auth.models import User
import json
# from decimal import Decimal
# from django.utils.text import slugify
# from uuid import uuid4
# import os

class All_Location(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=100)
    center =models.CharField(max_length=100) 
    # center = geomodels.PointFiel()  
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children'
    )
    location_type = models.CharField(max_length=20)
    country_code = models.CharField(max_length=2)
    state_abbr = models.CharField(max_length=3, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Accommodation(models.Model):
    feed = models.PositiveSmallIntegerField(default=0)  # Unsigned small integer
    title = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)  # ISO country code
    bedroom_count = models.PositiveIntegerField()  # Unsigned integer
    review_score = models.DecimalField(max_digits=3, decimal_places=1, default=0)  # Numeric with 1 decimal place
    usd_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Price rate in USD
    images = models.JSONField()  # Array of image URLs (max 300 characters per URL)
    amenities = models.JSONField()  # JSONB array of amenities
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Foreign key to User
    published = models.BooleanField(default=False)  # Boolean for published status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates

    def __str__(self):
        return self.title


class LocalizeAccommodation(models.Model):
    id=models.AutoField(primary_key=True)
    property = models.ForeignKey(
        'Accommodation',
        on_delete=models.CASCADE,
        related_name='localized'
    )
    language = models.CharField(max_length=2, choices=[('en', 'English'), ('bn', 'Bengali')])
    description = models.TextField()
    policy = models.JSONField(null=True,blank=True)


    # class Meta:
    #     unique_toghether=('property','language');
    #     verbose_name="Localized Accommodation"
    #     verbose_name_plural="Localized Accommodations"

    def __str__(self):
        return self.language
    


class Localize(models.Model):
    aaa = models.PositiveSmallIntegerField(default=0)  # Unsigned small integer
    bbb = models.CharField(max_length=100)
    ccc = models.CharField(max_length=2)  # ISO country code
    ddd = models.PositiveIntegerField()  # Unsigned integer