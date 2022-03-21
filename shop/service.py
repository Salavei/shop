from django.core.mail import send_mail


def send_regist(user_email, username, password):
    send_mail(
        'Вы успешно зарегестировались на сайте Sphere candle! Добро пожаловать',
        f'Ваш логин {username} , пароль {password} . Предотвращайте попаданию третьим лицам\nНастоятельно Вам рекомендуем указать ваш адрес в личном кабинете',
        'kano.hideyoshi@mail.ru',
        [user_email], fail_silently=False)


def send_buy(user_email, username, volume, structure, flavor, price, address):
    send_mail(
        'Вы успешно сделали заказ стандартная свеча Sphere candle!',
        f'{username}, Ваш заказ на этапе формирования!\nОбъем мл: {volume}\nСостав: {structure}\nАромат: {flavor}\nСтоимость {price}\nАдрес доставки: {address}',
        'kano.hideyoshi@mail.ru',
        [user_email], fail_silently=False)


def send_castom(user_email, username, candle_t, candle_color, candle_volume, candle_flavor, address):
    send_mail(
        'Вы успешно сделали заказ кастомная свеча Sphere candle!',
        f'{username}, Ваш заказ на этапе формирования!\nТип свечи: {candle_t}\nЦвет: {candle_color}\nОбъем мл: {candle_volume}\nАромат: {candle_flavor}\nСтоимость 35.00 BYN\nАдрес доставки: {address}',
        'kano.hideyoshi@mail.ru',
        [user_email], fail_silently=False)
