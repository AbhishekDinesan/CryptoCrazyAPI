from django.db import models

class crypto(models.Model):
    date = models.DateField()
    rank = models.DecimalField(max_digits=3, decimal_places=0)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    change = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.DecimalField(max_digits=20, decimal_places=2)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name