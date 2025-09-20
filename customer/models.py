from django.db import models
import uuid

class Customer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fantasy_name = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=14, unique=True) 
    cnpj_formated = models.CharField(max_length=18) 
    address = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'customer'