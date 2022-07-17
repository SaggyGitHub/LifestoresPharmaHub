from django.db import models

# Create your models here.
class Pharma(models.Model):
    name = models.CharField(max_length=265)
    description = models.TextField()
    sku = models.CharField(max_length=265)
    price = models.BigIntegerField()
    image = models.URLField()

    def __str__(self):
        return self.name