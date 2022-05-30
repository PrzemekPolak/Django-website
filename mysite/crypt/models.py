from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from .utils import *


class User_additional_data(models.Model):
    id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    wallet = models.IntegerField()

class Coin(models.Model):
    coin_id = models.CharField(max_length=10, primary_key=True)
    coin_name = models.CharField(max_length=20)
    def __str__(self):
        return self.coin_name
    
    # def get_cp():
    #     coins = Coin.objects.all()
    #     cp_list = []
    #     for c in coins:
    #         try:
    #             data = Coins_daily_data.get_data_from_x_hours_ago(c.coin_id, 1)
    #             data_f = data[len(data)-1].price/10000
    #             cp_list.append(data_f)
    #         except:
    #             cp_list.append('brak danych')
    #     return coins, cp_list

    def get_cp():
        coins = Coin.objects.all()
        cp_list = []
        for c in coins:
            try:
                data = Coins_daily_data.get_data_from_x_hours_ago(c.coin_id, 1)
                data_f = data[len(data)-1].price/10000
                cp_list.append(data_f)
            except:
                cp_list.append('brak danych')
        return cp_list

class Coins_data(models.Model):
    coins = models.ForeignKey(Coin, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    price = models.IntegerField()

    def get_data_from_x_days_ago(coin_id, last_x_days):
        current_datetime = datetime.now()
        # na potrzeby testowania narzucona data
        current_datetime = current_datetime.replace(year=2022, month=2, day=18)
        # -------------------------------------
        previous_datetime = current_datetime - timedelta(days=last_x_days)
        
        return Coins_data.objects.filter(coins=coin_id,
                                        date_time__lte=(current_datetime),
                                        date_time__gte=(previous_datetime))

    def get_time(coin_id, last_x_days):
        data = Coins_data.get_data_from_x_days_ago(coin_id, last_x_days)
        return list(map(lambda x: x.date_time.strftime("%Y:%m:%d"), data))

    def get_price(coin_id, last_x_days):
        data = Coins_data.get_data_from_x_days_ago(coin_id, last_x_days)
        return list(map(lambda x: x.price/10000, data))

class Coins_daily_data(models.Model):
    coins = models.ForeignKey(Coin, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    price = models.IntegerField()
    
    def get_data_from_x_hours_ago(coin_id, last_x_hours):
        current_datetime = datetime.now()
        # na potrzeby testowania narzucona data
        current_datetime = current_datetime.replace(year=2022, month=2, day=18)
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
    average_price = models.FloatField(null=True)
    class Meta:
        unique_together = (('user_id', 'coins'),)

class Transaction_history(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    BUY = 1
    SELL = 2
    TRANSACTION_TYPE = (
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    )
    transaction_type = models.PositiveSmallIntegerField(
        choices=TRANSACTION_TYPE,
    )
    coins = models.ForeignKey(Coin, on_delete=models.CASCADE)
    coins_amount = models.IntegerField()
    total_value = models.FloatField()

# TODO: Change fields from integer to float