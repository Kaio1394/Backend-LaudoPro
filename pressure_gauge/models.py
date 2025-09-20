from django.db import models
import uuid

class GaugeType(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "gauge_type"

class PressureGauge(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(max_length=200)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=15)
    resolution = models.CharField(max_length=20)                 
    rbc_certificate_number = models.CharField(max_length=50)     
    calibration_date = models.DateField()                         
    organization = models.CharField(max_length=100)
    gauge_type = models.ForeignKey(GaugeType, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.model} - {self.serial_number}"
    
    class Meta:
        db_table = "pressure_gauge"