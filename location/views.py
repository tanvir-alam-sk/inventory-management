from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from .models import All_Location

# Create your views here.

def index(request):
    return HttpResponse("Welcome to PostGreSQl")

def all_location(request):
    location = All_Location.objects.create(
        id="2",
        title="Los Angeles",
        center=Point(-118.2437, 34.0522),  # Longitude, Latitude
        location_type="City",
        country_code="US",
        state_abbr="CA",
        city="Los Angeles"
    )

    return JsonResponse({"message": f"Location {location.title} created successfully."})
