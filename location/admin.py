from django.contrib import admin
from .models import All_Location,Accommodation,Localize,LocalizeAccommodation





# Register your models here.
@admin.register(All_Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'center', 'location_type', 'country_code', 'city', 'created_at')
    search_fields = ('title', 'country_code', 'city')
    list_filter = ('location_type', 'country_code')


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('feed', 'title', 'country_code', 'bedroom_count', 'review_score', 'usd_rate', 'images', 'amenities', 'user_id', 'published', 'created_at', 'updated_at')
    search_fields = ('title', 'country_code', 'user_id')
    list_filter = ('country_code', 'published')


@admin.register(LocalizeAccommodation)
class LocalizeAccommodationAdmin(admin.ModelAdmin):
    list_display = ('language', 'description', 'policy')
    search_fields = ('language','description')
    list_filter = ('language','policy')

# @admin.register(Localize)
# class LocalizeAdmin(admin.ModelAdmin):
#     list_display = ('aaa', 'bbb', 'ccc', 'ddd')
#     search_fields = ('aaa', 'bbb')
#     list_filter = ('aaa','ddd')

