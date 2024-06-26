# Generated by Django 5.0.3 on 2024-04-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=50, unique=True, verbose_name='Слаг')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Изображение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('published', models.BooleanField(default=True, verbose_name='Признак публикации')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
