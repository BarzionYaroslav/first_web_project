from django.db import models
from django.core.validators import MinValueValidator 
from decimal import Decimal
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32,null=False,blank=False)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=256,null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    price = models.DecimalField(max_digits=16,decimal_places=2,null=False,blank=False, validators=[MinValueValidator(Decimal('0.01'))])
    stock = models.PositiveIntegerField(null=False,blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_images/', verbose_name='Изображение', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"