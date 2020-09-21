from django.db import models


class Places(models.Model):
    name = models.CharField(max_length=255)
    address_state = models.CharField(max_length=255) #estado
    address_city = models.CharField(max_length=255,null=True, blank=True) #cidade
    address_neighborhood = models.CharField(max_length=255,null=True, blank=True) # bairro
    address_complement = models.TextField(null=True, blank=True) # bairro
    create_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name
