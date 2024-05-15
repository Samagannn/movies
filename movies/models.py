import datetime

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории", unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название тега")

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    image = models.ImageField(upload_to='images/', verbose_name="Image", null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    content = models.TextField(verbose_name="Content")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category", blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name="Tag", blank=True)
    data = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Author')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product", related_name="images")
    image = models.ImageField(upload_to='image/', verbose_name="Images", null=True)

    def __str__(self):
        return str(self.product);


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product", related_name="attributes")
    name = models.CharField(max_length=150, verbose_name="Attribute Name")
    value = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Value")

    def __str__(self):
        return f"{self.product.title} - {self.name}: {self.value}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_url = models.URLField()
    mobile = models.CharField(max_length=20, default='999-999-9999')
    funds = models.FloatField(default=2000)

    def __str__(self):
        return "[Profile]" + self.user.username


class Log(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    message = models.TextField()

    def __str__(self):
        return self.message

# Create your models here.
