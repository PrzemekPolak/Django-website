from django.contrib.auth.models import User
from crypt.models import Coin, Coins_data, Coins_daily_data
from datetime import datetime
import json
from pycoingecko import CoinGeckoAPI


def conv_dt(tso):
    ts = int(tso)
    ts /= 1000
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def to_db(data, coinid, daily):
    for entry in data['prices']:
        dat = conv_dt(entry[0])
        pri = int(entry[1] * 10000)
        # upload to db !! only daily !!
        if daily == True:
            coin = Coin.objects.get(coin_id=coinid)
            c = Coins_daily_data(coins= coin, date_time=dat, price=pri)
            c.save()
        # upload to db !! not daily !!
        else:
            coin = Coin.objects.get(coin_id=coinid)
            c = Coins_data(coins= coin, date_time=dat, price=pri)
            c.save()


# user = User.objects.create_user('Przemek', 'przemek@example.com', 'przemyslaw')
# user.save()

# c = Coin(coin_id='BTC', coin_name='Bitcoin')
# c.save()
# c = Coin(coin_id='ETH', coin_name='Ethereum')
# c.save()

# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_range_by_id(id='ethereum', vs_currency='eur', from_timestamp='1645056000', to_timestamp='1645142399')
# to_db(cg, 'ETH', True)
# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_range_by_id(id='ethereum', vs_currency='eur', from_timestamp='1645142400', to_timestamp='1645228799')
# to_db(cg, 'ETH', True)

# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp='1645056000', to_timestamp='1645142399')
# to_db(cg, 'BTC', True)
# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp='1645142400', to_timestamp='1645228799')
# to_db(cg, 'BTC', True)

# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='eur', days=200)
# to_db(cg, 'ETH', False)

# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='eur', days=200)
# to_db(cg, 'BTC', False)


# c = Coin(coin_id='USDT', coin_name='Tether')
# c.save()
# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_range_by_id(id='tether', vs_currency='eur', from_timestamp='1645056000', to_timestamp='1645142399')
# to_db(cg, 'USDT', True)
# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_range_by_id(id='tether', vs_currency='eur', from_timestamp='1645142400', to_timestamp='1645228799')
# to_db(cg, 'USDT', True)
# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_by_id(id='tether', vs_currency='eur', days=200)
# to_db(cg, 'USDT', False)

# c = Coin(coin_id='DOGE', coin_name='Dogecoin')
# c.save()
# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_range_by_id(id='dogecoin', vs_currency='eur', from_timestamp='1645056000', to_timestamp='1645142399')
# to_db(cg, 'DOGE', True)
# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_range_by_id(id='dogecoin', vs_currency='eur', from_timestamp='1645142400', to_timestamp='1645228799')
# to_db(cg, 'DOGE', True)
# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_by_id(id='dogecoin', vs_currency='eur', days=200)
# to_db(cg, 'DOGE', False)

# c = Coin(coin_id='LTC', coin_name='Litecoin')
# c.save()
# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_range_by_id(id='litecoin', vs_currency='eur', from_timestamp='1645056000', to_timestamp='1645142399')
# to_db(cg, 'LTC', True)
# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_range_by_id(id='litecoin', vs_currency='eur', from_timestamp='1645142400', to_timestamp='1645228799')
# to_db(cg, 'LTC', True)
# cg = CoinGeckoAPI()
# cg = cg.get_coin_market_chart_by_id(id='litecoin', vs_currency='eur', days=200)
# to_db(cg, 'LTC', False)
