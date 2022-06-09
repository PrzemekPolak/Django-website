from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import CoinSerializer, User_assetSerializer, Transaction_historySerializer
from crypt.models import Transaction_history, User_asset, Coin, Coins_daily_data, Coins_data, User_additional_data
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime


class get_coin_name(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    def get_queryset(self):
        coin_id = self.kwargs.get('coin_id')
        return Coin.objects.filter(coin_id=coin_id)

def coin_list(request):
    if(request.method == 'GET'):
        data = list(Coin.objects.values())
        cp_data = Coin.get_cp()
        for x in range(len(data)):
            data[x]['current_price'] = cp_data[x]        
        return JsonResponse(data,safe=False)


def coin_get_price(request, coin_id, time_range):
    chart_time = Coins_daily_data.get_time(coin_id, time_range)
    chart_price = Coins_daily_data.get_price(coin_id, time_range)
    coin_data = {
        'labels': chart_time,
        'data': chart_price,
    }
    return JsonResponse(coin_data,safe=False)

def coin_get_price_old(request, coin_id, time_range):
    chart_time = Coins_data.get_time(coin_id, time_range)
    chart_price = Coins_data.get_price(coin_id, time_range)
    coin_data = {
        'labels': chart_time,
        'data': chart_price,
    }   
    return JsonResponse(coin_data,safe=False)

@csrf_exempt
def user_login(request):
    # if request.method == "POST":
    data = JSONParser().parse(request)
    username = data['uname']
    password = data['psw']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        add_data = User_additional_data.objects.get(id=user.id)
        cash = add_data.wallet
        return JsonResponse({'logged': True,'user': user.username, 'user_id': user.id, 'cash': cash, 'failed_login': False},safe=False)
    else:
        return JsonResponse({'logged': False, 'user': None, 'user_id': None, 'cash': None, 'failed_login': True},safe=False)

@csrf_exempt
def user_logout(request):
    logout(request)   
    return JsonResponse({'success': True,},safe=False)

class get_user_assets(viewsets.ModelViewSet):
    queryset = User_asset.objects.all()
    serializer_class = User_assetSerializer
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        coin_id = self.kwargs.get('coin_id')
        if coin_id:
            # Get only specific coin of one user
            assets = User_asset.objects.filter(user_id=user_id, coins=coin_id)
        else:
            # Get all assets of one user
            assets = User_asset.objects.filter(user_id=user_id)
        return assets

@csrf_exempt
def coin_buy(request):    
    data = JSONParser().parse(request)
    coin_id = data['coin_id']
    form_amount = float(data['form_amount'])
    user_id = data['user_id']

    user = User.objects.get(id=user_id)
    coin = Coin.objects.get(coin_id=coin_id)
    timestamp = datetime.datetime.now()

    # Check if there is enough cash for transaction
    user_cash = User_additional_data.objects.get(id=user_id)
    current_price = Coins_daily_data.get_price(coin_id, 2)[-1]
    total = current_price * form_amount
    if user_cash.wallet < total:
        return JsonResponse({'success': False, 'error': 'Insufficient cash'},safe=False)

    # Check if coresponding record exist. If true then modify it, else create a new record
    # Update amount of cash and average price. Add record to transaction history
    already_exist = User_asset.objects.filter(user_id=user, coins=coin)
    if already_exist:
        current_amount = already_exist[0].amount
        new_amount = current_amount + form_amount
        already_exist[0].amount = new_amount
        new_average_price = (already_exist[0].average_price * current_amount) + (form_amount * current_price)
        already_exist[0].average_price = new_average_price / new_amount
        already_exist[0].save()
        user_cash.wallet -= total
        user_cash.save()
        transaction_history = Transaction_history(user_id=user, date_time=timestamp, transaction_type=1, coins=coin, coins_amount=form_amount, total_value=total)
        transaction_history.save()
        return JsonResponse({'success': True, 'amount': already_exist[0].amount, 'cash': user_cash.wallet},safe=False)
    else:
        u_asset = User_asset(user_id=user, coins=coin, amount=form_amount, average_price=current_price)
        u_asset.save()
        user_cash.wallet -= total
        user_cash.save()
        transaction_history = Transaction_history(user_id=user, date_time=timestamp, transaction_type=1, coins=coin, coins_amount=form_amount, total_value=total)
        transaction_history.save()
        return JsonResponse({'success': True, 'amount': u_asset.amount, 'cash': user_cash.wallet},safe=False)

@csrf_exempt
def coin_sell(request):
    data = JSONParser().parse(request)
    # Check if correct date type
    try:
        coin_id = data['coin_id']
        form_amount = float(data['form_amount'])
        user_id = data['user_id']
    except:
        return JsonResponse({'success': False,
            'error': 'Wrong data type'},safe=False)
    user = User.objects.get(id=user_id)
    coin = Coin.objects.get(coin_id=coin_id)
    timestamp = datetime.datetime.now()
    existing_asset = User_asset.objects.get(user_id=user, coins=coin)    
    # Check if user has enough coins and buy more than 0
    if existing_asset.amount < form_amount and form_amount > 0:
        return JsonResponse({'success': False,
            'error': 'Insufficient coins amount or buying less than 0'},
            safe=False)
    user_cash = User_additional_data.objects.get(id=user_id)
    current_price = Coins_daily_data.get_price(coin_id, 2)[-1]
    total = current_price * form_amount
    # Update amount of cash and coins
    user_cash.wallet += total
    user_cash.save()
    current_amount = existing_asset.amount
    new_amount = current_amount - form_amount
    existing_asset.amount = new_amount   
    existing_asset.save()
    # Add transaction history
    transaction_history = Transaction_history(user_id=user,
        date_time=timestamp, transaction_type=2,
        coins=coin, coins_amount=form_amount, total_value=total)
    transaction_history.save()
    return JsonResponse({'success': True,
        'amount': existing_asset.amount, 'cash': user_cash.wallet},
        safe=False)

class get_user_transactions(viewsets.ModelViewSet):
    queryset = Transaction_history.objects.all()
    serializer_class = Transaction_historySerializer
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Transaction_history.objects.filter(user_id=user_id).order_by('-date_time')

