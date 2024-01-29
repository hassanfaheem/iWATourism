from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Package)
admin.site.register(Booking)
admin.site.register(Customer)

class ItineraryAdmin(admin.StackedInline):
    model = Itinerary

class PackageAdmin(admin.StackedInline):
    model = Package

class AddOnAdmin(admin.StackedInline):
    model = AddOn

@admin.register(GroupTour)
class GroupTourAdmin(admin.ModelAdmin):
    inlines = [ItineraryAdmin, PackageAdmin, AddOnAdmin]
    class Meta:
       model = GroupTour
