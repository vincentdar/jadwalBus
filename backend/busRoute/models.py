from django.db import models
from region.models import Province, City

# Create your models here.
class Terminal(models.Model):
    city = models.ForeignKey("region.City", on_delete=models.RESTRICT)
    name = models.CharField(max_length=50, blank=False, default='')

    def __str__(self):
        return str(self.city) + " | " + str(self.name)
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Terminal"
        verbose_name_plural = "Terminals"
    
class Bus(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    address = models.CharField(max_length=50, blank=True, default='')
    phone_number = models.CharField(max_length=50, blank=True, default='')
    information = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Bus"
        verbose_name_plural = "Buses"

class Route(models.Model):        
    bus = models.ForeignKey("busRoute.Bus", on_delete=models.RESTRICT, related_name="bus")
    # Sediakan nama Kota dipisah pake ";"
    route = models.TextField(blank=True, default='')
    departure_terminal = models.ForeignKey("busRoute.Terminal", on_delete=models.RESTRICT, related_name='departure_terminal')
    destination_terminal = models.ForeignKey("busRoute.Terminal", on_delete=models.RESTRICT, related_name='destination_terminal')
    time_departure = models.TimeField()
    time_arrival = models.TimeField()
    seat = models.BigIntegerField(blank=True, null=True)
    price = models.DecimalField(blank=True, max_digits=15, decimal_places=2, null=True)

    def __str__(self):        
        return str(self.bus) + " | " + str(self.departure_terminal) + " - " + str(self.destination_terminal)
       
    class Meta:
        ordering = ('id',)
        verbose_name = "route"
        verbose_name_plural = "routes"
