from django.contrib import admin
from .models import Places, PersonInChargeOf, DivingEvents

# Register your models here.

class PlacesAdmin(admin.ModelAdmin):
    """This class customizes the admin interface for the 'Places' table."""

    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Places, PlacesAdmin)

class PersonInChargeOfAdmin(admin.ModelAdmin):
    """This class customizes the admin interface for the 'PersonInChargeOf'
    table."""
    
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(PersonInChargeOf, PersonInChargeOfAdmin)

class DivingEventsAdmin(admin.ModelAdmin):
    """This class customizes the admin interface for the 'DivingEvents' 
    table."""

    list_display = ('date', 'place', 'person', 'extra_infos',)
    list_filter = ('place', 'person',)
    ordering = ('date',)
    search_fields = ('extra_infos',)

admin.site.register(DivingEvents, DivingEventsAdmin)
