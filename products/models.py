from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    make_company = models.CharField(max_length=50)
    composition = models.CharField(max_length=250)
    make_year = models.DateField()
    limit_year = models.DateField()
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title