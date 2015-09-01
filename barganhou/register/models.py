from django.db import models

class ProductInfo (models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    amount = models.IntegerField()
    date_log = models.DateField()
    local = models.CharField(max_length=30)
    pucharse = models.CharField(max_length=3,
                                choices=(('Y', 'yes'), ('N', 'no')))
    
    def list(self):
        return [self.name, self.price, self.amount, self.local]

    def dict(self):
        return {'name': self.name, 'price': str(self.price), 
            'amount': self.amount, 'local': self.local, 'id': self.pk}
    
    def __str__(self):
        return self.name