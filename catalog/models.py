from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(
        upload_to="product/", verbose_name="Изображение", null=True, blank=True
    )
    category = models.ForeignKey(
        "catalog.Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания (записи в БД)"
    )
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата последнего изменения (записи в БД)"
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.name} | {self.description}"

    class Meta:
        verbose_name = "Продукт"  # Настройка для наименования одного объекта
        verbose_name_plural = "Продукты"  # Настройка для наименования набора объектов


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.name} | {self.description}"

    class Meta:
        verbose_name = "Категория"  # Настройка для наименования одного объекта
        verbose_name_plural = "Категории"  # Настройка для наименования набора объектов


class Version(models.Model):
    name = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE, related_name='versions')
    version_number = models.PositiveIntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name="Название версии")
    version_now = models.BooleanField(
        default=True, verbose_name="Признак текущей версии"
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.version_name} | {self.version_number}"


    class Meta:
        verbose_name = "Версия"  # Настройка для наименования одного объекта
        verbose_name_plural = "Версии"  # Настройка для наименования набора объектов
