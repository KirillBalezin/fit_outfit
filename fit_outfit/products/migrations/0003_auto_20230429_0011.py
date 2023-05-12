# Generated by Django 2.2.16 on 2023-04-28 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230428_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(help_text='Напишите описание категории', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='Введите название категории', max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Категория, товара', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(help_text='Напишите описание товара', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(help_text='Введите название товара', max_length=200, verbose_name='Название товара'),
        ),
    ]