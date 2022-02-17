from django.contrib import admin

from .models import Coin, Coins_data, Coins_daily_data

admin.site.register(Coin)
admin.site.register(Coins_data)
admin.site.register(Coins_daily_data)