from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    base_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Базовая цена")
    sort_order = models.IntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE, verbose_name="Товар")
    image = models.ImageField(upload_to="catalog/product_images/", verbose_name="Файл")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Подпись")
    sort_order = models.IntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображение товаров"

    def __str__(self):
        return f"{self.product.name} - {self.caption}"


class ProductParameter(models.Model):
    product = models.ForeignKey(Product, related_name="parameters", on_delete=models.CASCADE, verbose_name="Товар")
    name = models.CharField(max_length=200, verbose_name="Название")
    value = models.CharField(max_length=200, verbose_name="Значение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", null=True, blank=True)
    sort_order = models.IntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "Параметры товара"
        verbose_name_plural = "Параметры товаров"

    def __str__(self):
        return f"{self.product.name} - {self.name}: {self.value}"
