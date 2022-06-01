from django.urls import path
from . import views

urlpatterns = [
    # ex: /api/
    # path('', views.user_asset),#.as_view({'get': 'list'})),
    # path('<int:pk>/', views.user_asset_detail),

    path('coin_list/', views.coin_list),#.as_view({'get': 'list'})),
    path('coin_get_price/<str:coin_id>/<int:time_range>', views.coin_get_price),
    path('coin_get_price/old/<str:coin_id>/<int:time_range>', views.coin_get_price_old),
    path('user_login/', views.user_login),
    path('user_logout/', views.user_logout),
    path('coin_buy/', views.coin_buy),
    path('coin_sell/', views.coin_sell),
    path('get_user_assets/<str:user_id>/', views.get_user_assets.as_view({'get': 'list'})),
    path('get_user_assets/<str:user_id>/<str:coin_id>/', views.get_user_assets.as_view({'get': 'list'})),
]