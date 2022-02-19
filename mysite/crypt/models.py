from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class User_additional_data(models.Model):
    id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    wallet = models.IntegerField()

class Coin(models.Model):
    coin_id = models.CharField(max_length=10, primary_key=True)
    coin_name = models.CharField(max_length=20)
    def __str__(self):
        return self.coin_name

class Coins_data(models.Model):
    coins = models.ForeignKey(Coin, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    price = models.IntegerField()
    def __str__(self):
        return f'Date: {self.date}\nPrice: {self.price}'

class Coins_daily_data(models.Model):
    coins = models.ForeignKey(Coin, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    price = models.IntegerField()
    def __str__(self):
        return f'Date: {self.date_time}\nPrice: {self.price}'

    
    def get_data_from_x_hours_ago(coin_id, last_x_hours):
        def date_set_format(date_time):
            date = date_time.date()
            hour = date_time.hour
            minute = date_time.minute
            second = date_time.second
            return f'{date} {hour}:{minute}:{second}'
        
        current_datetime = datetime.now()
        # na potrzeby testowania narzucona data
        current_datetime = current_datetime.replace(year=2022, month=2, day=15)
        # -------------------------------------
        c_time = date_set_format(current_datetime)

        previous_datetime = current_datetime - timedelta(hours=last_x_hours)
        p_time = date_set_format(previous_datetime)
        
        return Coins_daily_data.objects.filter(coins=coin_id,
                                            date_time__lte=(c_time),
                                            date_time__gte=(p_time))
     
    def get_time(coin_id, last_x_hours):
        data = Coins_daily_data.get_data_from_x_hours_ago(coin_id, last_x_hours)
        return list(map(lambda x: x.date_time.strftime("%H:%M:%S"), data))

    def get_price(coin_id, last_x_hours):
        data = Coins_daily_data.get_data_from_x_hours_ago(coin_id, last_x_hours)
        return list(map(lambda x: x.price/10000, data))

class User_asset(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coins = models.ForeignKey(Coin, on_delete=models.CASCADE)
    ammount = models.IntegerField()
    class Meta:
        unique_together = (('user_id', 'coins'),)