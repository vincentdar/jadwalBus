from django.db import models

# Create your models here.
class Province(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

class City(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    province = models.ForeignKey("region.Province", on_delete=models.RESTRICT)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ["id"]
        verbose_name = "City"
        verbose_name_plural = "Cities"

class District(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    city = models.ForeignKey("region.City", on_delete=models.RESTRICT)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ["id"]
        verbose_name = "District"
        verbose_name_plural = "Districts"

class Village(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    district = models.ForeignKey("region.District", on_delete=models.RESTRICT)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Village"
        verbose_name_plural = "Villages"

