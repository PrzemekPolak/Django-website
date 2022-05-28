from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import User_assetSerializer
from crypt.models import User_asset, Coin, Coins_daily_data, Coins_data, User_additional_data
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie

# def coin_list(request):
    # if(request.method == 'GET'):
    #     data = Coin.get_cp()
    #     data = ser.serialize('json', Coin.get_cp(), fields=('coin_id','coin_name','price'))
    #     return JsonResponse(data,safe=False)

# class coin_list(viewsets.ModelViewSet):
#     queryset = Coin.objects.all()
#     serializer_class = Coin_listSerializer

# @login_required
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




def coin_buy(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        coin_id = data['coin_id']
        form_amount = data['form_amount']
        user_id = data['user_id']

        coin = Coin.objects.get(coin_id=coin_id)
        u_asset = User_asset(user_id=user_id, coins=coin, ammount=form_amount)
        u_asset.save()
        return JsonResponse({'success': True},safe=False)
