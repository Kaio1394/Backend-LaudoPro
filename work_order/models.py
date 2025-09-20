from django.db import models
import uuid

class WorkOrder(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    work_order_number = models.CharField(max_length=20, unique=True, blank=True)
    calibration_date = models.DateField(null=True, blank=True)
    validate_date = models.DateField(null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = 'worder_order'
