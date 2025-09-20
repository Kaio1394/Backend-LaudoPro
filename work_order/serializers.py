from rest_framework import serializers
from .models import WorkOrder

class WorkOrderSerializer(serializers.ModelSerializer):
    model = WorkOrder
    fields = ["work_order_number", "calibration_date", "validate_date", "issue_date"]