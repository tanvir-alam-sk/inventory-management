from django.contrib import admin
from .models import Location

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location_type', 'country_code', 'city', 'created_at')
    search_fields = ('title', 'country_code', 'city')
    list_filter = ('location_type', 'country_code')
