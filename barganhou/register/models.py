from django.db import models
from datetime import date

states = (('AC', 'Acre'),
          ('AL', 'Alagoas'),
          ('AP', 'Amapá'),
          ('AM', 'Amazonas'),
          ('BA', 'Bahia'),
          ('CE', 'Ceará'),
          ('DF', 'Distrito Federal'),
          ('ES', 'Espírito Santo'),
          ('GO', 'Goiás'),
          ('MA', 'Maranhão'),
          ('MT', 'Mato Grosso'),
          ('MS', 'Mato Grosso do Sul'),
          ('MG', 'Minas Gerais'),
          ('PA', 'Pará'),
          ('PB', 'Paraíba'),
          ('PR', 'Paraná'),
          ('PE', 'Pernambuco'),
          ('PI', 'Piauí'),
          ('RJ', 'Rio de Janeiro'),
          ('RN', 'Rio Grande do Norte'),
          ('RS', 'Rio Grande do Sul'),
          ('RO', 'Rondônia'),
          ('RR', 'Roraima'),
          ('SC', 'Santa Catarina'),
          ('AP', 'São Paulo'),
          ('SE', 'Sergipe'),
          ('TO', 'Tocantins')
         )

class LocalInfo (models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=19, default='AL', choices=states)
    city = models.CharField(max_length=50, default='Maceió')
    cep = models.IntegerField(blank=True, null=True)
    street = models.CharField(max_length=300)
    number = models.IntegerField(blank=True, null=True)
    neighborhood = models.CharField(max_length=200)

    def dict(self):
        return {'name': self.name, 'state': self.state, 'city': self.city, 
            'cep': str(self.cep), 'street': self.street, 
            'number': str(self.number), 'neighborhood': self.neighborhood,
            'id': self.pk}
    
    def __str__(self):
        return self.name
         

class ProductInfo (models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    amount = models.IntegerField()
    date_log = models.DateField(default=date.today)
    local = models.ForeignKey(LocalInfo)
    pucharse = models.CharField(max_length=3, default='Y',
                                choices=(('Y', 'yes'), ('N', 'no')))

    def dict(self):
        return {'name': self.name, 'price': str(self.price), 
            'amount': self.amount, 'local': str(self.local),
            'local_id': self.local.pk, 'id': self.pk}
    
    def __str__(self):
        return self.name








