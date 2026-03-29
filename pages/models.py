from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=256,null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    price = models.DecimalField(max_digits=16,decimal_places=2,null=False,blank=False)
    stock = models.PositiveIntegerField(null=False,blank=False)

    def __str__(self) -> str:
        return f"{self.name}: {self.stock}"