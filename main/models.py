from django.db import models

# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class  Product(models.Model):
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    info = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='img')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name