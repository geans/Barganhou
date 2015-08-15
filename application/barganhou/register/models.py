from django.db import models

# Create your models here.
class ProductInfo (models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_log = models.DateField()
    local = models.CharField(max_length=30)
    pucharse = models.CharField(max_length=3,
                                choices=(('Y', 'yes'), ('N', 'no')))
    
    def __str__(self):
        return self.name
