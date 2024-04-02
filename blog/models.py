from django.db import models

NULL_PARAM = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=50, unique=True, verbose_name='Слаг', **NULL_PARAM)
    content = models.TextField(verbose_name='Содержимое', **NULL_PARAM)
    preview = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULL_PARAM)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title} {self.slug}, просмотров: {self.views}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
