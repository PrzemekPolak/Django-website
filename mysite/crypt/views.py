from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic

from .models import Coin, Coins_data, Coins_daily_data

# def index(request):
#     coins = get_list_or_404(Coin)
#     return render(request, 'crypt/index.html', {'coins': coins})
class index(generic.ListView):
    template_name = 'crypt/index.html'
    context_object_name = 'coins'
    def get_queryset(self):
        return Coin.objects.all()

def detail(request, coin_id):
    coins_data = Coins_data.objects.filter(coins=coin_id)
    return render(request, 'crypt/detail.html', {'coin_id': coin_id,
        'coins_data': coins_data})

def user_log_in(request, failed=False):
    return render(request, 'crypt/user_log_in.html', {'failed': failed})

def user_log_in_form(request):
    username = request.POST['uname']
    password = request.POST['psw']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # roboczo
        return redirect('/crypt/')

    else:
        return redirect('/crypt/login_failed')

def login_failed(request):
    failed = True
    return render(request, 'crypt/user_log_in.html', {'failed': failed})

def user_log_out(request):
    logout(request)
    return redirect('/crypt/')







def update_db_button(request):
    #import load_to_db
    return redirect('/crypt/')