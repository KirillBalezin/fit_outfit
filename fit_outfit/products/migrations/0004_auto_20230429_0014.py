# Generated by Django 2.2.16 on 2023-04-28 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230429_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, help_text='Напишите описание категории', null=True, verbose_name='Описание'),
        ),
    ]
