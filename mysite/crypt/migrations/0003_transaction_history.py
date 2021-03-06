# Generated by Django 4.0.2 on 2022-05-30 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crypt', '0002_user_asset_average_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('transaction_type', models.PositiveSmallIntegerField(choices=[(1, 'Buy'), (2, 'Sell')])),
                ('coins_amount', models.IntegerField()),
                ('total_value', models.FloatField()),
                ('coins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypt.coin')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
