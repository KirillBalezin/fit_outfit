# Generated by Django 2.2.16 on 2023-05-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20230430_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('Yes', 'Да'), ('No', 'Нет')], default='No', help_text='Есть ли размеры', max_length=5, verbose_name='Размеры'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_l',
            field=models.PositiveIntegerField(default=0, verbose_name='Размер L'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_m',
            field=models.PositiveIntegerField(default=0, verbose_name='Размер M'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_s',
            field=models.PositiveIntegerField(default=0, verbose_name='Размер S'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_xl',
            field=models.PositiveIntegerField(default=0, verbose_name='Размер XL'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_xxl',
            field=models.PositiveIntegerField(default=0, verbose_name='Размер XXL'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_xxxl',
            field=models.PositiveIntegerField(default=0, verbose_name='Размер XXXL'),
        ),
    ]
