from django.urls import path
from . import views

urlpatterns = [
    # ex: /crypt/
    path('', views.index.as_view(), name='index'),
    path('user_log_in/', views.user_log_in, name='user_log_in'),
    path('user_log_in_form/', views.user_log_in_form, name='user_log_in_form'),
    path('login_failed/', views.login_failed, name='login_failed'),
    path('user_log_out/', views.user_log_out, name='user_log_out'),
    path('detail/<str:coin_id>/<int:time_range>', views.detail, name='detail'),
    path('detail/old/<str:coin_id>/<int:time_range>', views.detail_old, name='detail_old'),
    



    path('update_db_button',views.update_db_button, name='update_db_button')
]