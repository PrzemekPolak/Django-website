# Generated by Django 4.0.2 on 2022-02-17 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('coin_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('coin_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User_additional_data',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('wallet', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coins_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('coins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypt.coin')),
            ],
        ),
        migrations.CreateModel(
            name='Coins_daily_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('coins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypt.coin')),
            ],
        ),
        migrations.CreateModel(
            name='User_asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.IntegerField()),
                ('coins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypt.coin')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_id', 'coins')},
            },
        ),
    ]
