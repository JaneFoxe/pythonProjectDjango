from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to='product/')
    category = models.models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} | {self.description}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = TextField()

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} | {self.description}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
