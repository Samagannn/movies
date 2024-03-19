from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")

    def str(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название тега")

    def str(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    content = models.TextField(verbose_name="Контент")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name="Теги", blank=True)

    def str(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт", related_name="images")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")

    def str(self):
        return str(self.product)


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт", related_name="attributes")
    name = models.CharField(max_length=150, verbose_name="Название атрибута")
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Значение")

    def str(self):
        return f"{self.product.title} - {self.name}: {self.value}"

# Create your models here.
