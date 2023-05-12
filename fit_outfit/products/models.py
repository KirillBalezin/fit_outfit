from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Введите название категории'
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        verbose_name='Ссылка',
        help_text='Напишите ссылку (только на английском)'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
        help_text='Напишите описание категории'
    )

    class Meta:
        default_related_name = 'categories'
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    CHOICES = (
        ('Yes', 'Да'),
        ('No', 'Нет')
    )
    title = models.TextField(
        max_length=200,
        verbose_name='Название товара',
        help_text='Введите название товара',
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Категория, товара',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
        help_text='Напишите описание товара'
    )
    price = models.PositiveIntegerField(
        'Цена',
        blank=True,
        null=True,
        default=0
    )
    purchase_price = models.PositiveIntegerField(
        'Закупочная цена',
        blank=True,
        null=True,
        default=0
    )
    size = models.CharField(
        max_length=5,
        choices=CHOICES,
        default='No',
        verbose_name='Размеры',
        help_text='Есть ли размеры'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='products/',
        blank=True,
    )
    amount = models.PositiveIntegerField(
        'Количество',
        default=0
    )
    size_s = models.PositiveIntegerField(
        'Размер S',
        default=0
    )
    size_m = models.PositiveIntegerField(
        'Размер M',
        default=0
    )
    size_l = models.PositiveIntegerField(
        'Размер L',
        default=0
    )
    size_xl = models.PositiveIntegerField(
        'Размер XL',
        default=0
    )
    size_xxl = models.PositiveIntegerField(
        'Размер XXL',
        default=0
    )
    size_xxxl = models.PositiveIntegerField(
        'Размер XXXL',
        default=0
    )

    class Meta:
        default_related_name = 'products'
        ordering = ['title']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
