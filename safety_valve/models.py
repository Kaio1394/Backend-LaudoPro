from django.db import models
import uuid

class SafetyValve(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=100, default='Safety Valve')
    tag = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100) 
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=20) 
    actuation_range = models.CharField(max_length=50) 