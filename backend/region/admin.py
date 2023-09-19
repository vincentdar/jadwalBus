from django.contrib import admin
from .models import Province, City, District, Village

# Register your models here.
@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    pass  

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass  

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass  

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    pass  

