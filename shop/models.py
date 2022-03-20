from django.db import models
from django.contrib.auth.models import User


class UUser(User):
    phone = models.CharField(max_length=12, unique=True, null=False)


class Order(models.Model):
    user_id = models.ForeignKey(User, related_name='user_ordering', null=False, on_delete=models.CASCADE)
    TYPE_CHOICES = (
        (1, 'figure'),
        (2, 'candle_standart'),
    )
    COLOR_CHOICES = (
        (1, 'WHITE'),
        (2, 'YELLOW'),
        (3, 'BLACK'),
    )
    FLAVOR_CHOICES = (
        (1, 'яблочный пирог'),
        (2, 'черный кокос'),
        (3, 'вечер у камина'),
        (4, 'ягодный пунш'),
        (5, 'сумеречный лес'),
    )
    VOLUME_CHOICES = (
        (1, '200'),
        (2, '100'),
    )
    STATUS_CHOICES = (
        ('In processing', 1),
        ('sent', 2),
    )
    candle_t = models.PositiveIntegerField(choices=TYPE_CHOICES)
    candle_color = models.PositiveIntegerField(choices=COLOR_CHOICES)
    candle_flavor = models.PositiveIntegerField(choices=FLAVOR_CHOICES)
    candle_volume = models.PositiveIntegerField(choices=VOLUME_CHOICES)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='1', db_index=True)
    created_order = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f'{self.user_id} - формирование заказа : {self.status}'

    class Meta:
        ordering = ('status', 'created_order')
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Product(models.Model):
    VOLUME_CHOICES = (
        (200, '200'),
        (100, '100'),
    )
    volume = models.PositiveIntegerField(choices=VOLUME_CHOICES)
    structure = models.CharField(max_length=256)
    flavor = models.CharField(max_length=256)
    img = models.ImageField(upload_to='static', null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField(null=True, db_index=True)

    def __str__(self):
        return f'{self.flavor} количество на складе : {self.count}'

    class Meta:
        ordering = ('count',)
        verbose_name = 'Свеча'
        verbose_name_plural = 'Свечи'
