# Generated by Django 2.2.16 on 2023-05-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Закупочная цена'),
        ),
    ]
