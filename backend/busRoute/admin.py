from django.contrib import admin
from .models import Bus, Terminal, Route

# Register your models here.
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    pass

@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = ("name", "city")    

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ("bus", "departure_terminal", "destination_terminal")

    fieldsets = [
        (None, {"fields": ["bus"]}),
        ("Routes", {"fields": ["departure_terminal", "destination_terminal", "route"]}),
        ("Time ", {"fields": ["time_departure", "time_arrival"]}),
        ("Additional Info", {"fields": ["seat", "price"]})
    ]
