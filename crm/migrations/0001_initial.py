# Generated by Django 4.1.7 on 2023-02-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_created', models.DateTimeField(auto_now=True)),
                ('order_name', models.CharField(max_length=200, verbose_name='Имя клиента')),
                ('order_phone', models.CharField(max_length=200, verbose_name='Телефон клиента')),
            ],
        ),
    ]
