from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = (
    ('фигура', 'фигура'),
    ('стандартная', 'стандартная'),
)
COLOR_CHOICES = (
    ('белый', 'белый'),
    ('желтый', 'желтый'),
    ('черный', 'черный'),
)
FLAVOR_CHOICES = (
    ('яблочный пирог', 'яблочный пирог'),
    ('черный кокос', 'черный кокос'),
    ('вечер у камина', 'вечер у камина'),
    ('ягодный пунш', 'ягодный пунш'),
    ('сумеречный лес', 'сумеречный лес'),
)
VOLUME_CHOICES = (
    (200, 200),
    (100, 100),
)
STATUS_CHOICES = (
    ('формируется', 'формируется'),
    ('отправлено', 'отправлено'),
)


class UUser(User):
    phone = models.CharField(max_length=13, unique=True, null=False)
    address = models.CharField(max_length=255, null=True, default='Отсутствует')


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ordering', null=False)

    candle_t = models.CharField(max_length=255, choices=TYPE_CHOICES)
    candle_color = models.CharField(max_length=255, choices=COLOR_CHOICES)
    candle_flavor = models.CharField(max_length=255, choices=FLAVOR_CHOICES)
    candle_volume = models.PositiveIntegerField(choices=VOLUME_CHOICES)
    address = models.CharField(max_length=255, default='Отсутствует')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='формируется', db_index=True)
    created_order = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f'{self.user_id} - формирование заказа : {self.status}'

    class Meta:
        ordering = ('status', 'created_order')
        verbose_name = 'Кастом'
        verbose_name_plural = 'Кастом'


class Product(models.Model):
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


class Buy(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_buy', null=False)
    volume = models.PositiveIntegerField(choices=VOLUME_CHOICES)
    structure = models.CharField(max_length=256)
    flavor = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='формируется', db_index=True)
    created_order = models.DateTimeField(auto_now_add=True, db_index=True)
    address = models.CharField(max_length=255, default='Отсутствует')

    def __str__(self):
        return f'{self.flavor}: {self.user_id}'

    class Meta:
        ordering = ('status', 'created_order')
        verbose_name = 'Стандартные'
        verbose_name_plural = 'Стандартные'
