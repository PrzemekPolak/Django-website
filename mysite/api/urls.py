from django.urls import path
from . import views

urlpatterns = [
    # ex: /api/
    path('', views.user_asset),#.as_view({'get': 'list'})),
    path('<int:pk>/', views.user_asset_detail),
]