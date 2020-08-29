from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode


# Create your models here.
class Department(models.Model):

    name = models.CharField()
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


class SubDepartment(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField()
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


class Product(models.Model):

    sub_department = models.ForeignKey(SubDepartment, on_delete=models.CASCADE)
    name = models.CharField('Name')
    price = models.FloatField(null=False)
    discount = models.FloatField(default=0)
    description = models.TextField(null=False)
    thumbnail = models.ImageField(upload_to='products', editable=True, null=False, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)


class Transaction(models.Model):
    pass