from django.urls import path
from . import views

urlpatterns = [
    # ex: /api/
    path('coin_list/', views.coin_list),
    path('get_coin_name/<str:coin_id>/', views.get_coin_name.as_view({'get': 'list'})),
    path('coin_get_price/<str:coin_id>/<int:time_range>', views.coin_get_price),
    path('coin_get_price/old/<str:coin_id>/<int:time_range>', views.coin_get_price_old),
    path('user_login/', views.user_login),
    path('user_logout/', views.user_logout),
    path('coin_buy/', views.coin_buy),
    path('coin_sell/', views.coin_sell),
    path('get_user_assets/<str:user_id>/', views.get_user_assets.as_view({'get': 'list'})),
    path('get_user_assets/<str:user_id>/<str:coin_id>/', views.get_user_assets.as_view({'get': 'list'})),
    path('get_user_transactions/<str:user_id>/', views.get_user_transactions.as_view({'get': 'list'})),
    path('fill_db_with_example_data/', views.fill_db_with_example_data),
]