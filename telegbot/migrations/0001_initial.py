# Generated by Django 4.1.3 on 2023-03-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_token', models.CharField(max_length=200, verbose_name='Токен')),
                ('tg_chat', models.CharField(max_length=200, verbose_name='Чат айди')),
                ('tg_message', models.TextField(verbose_name='Текст сообщания')),
            ],
            options={
                'verbose_name': 'Настройку',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]