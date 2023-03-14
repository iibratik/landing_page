# Generated by Django 4.1.7 on 2023-02-25 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsslider',
            name='slider_css',
            field=models.CharField(default='-', max_length=20, null=True, verbose_name='Активный слайд'),
        ),
        migrations.AlterField(
            model_name='cmsslider',
            name='slider_desr',
            field=models.CharField(max_length=200, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='cmsslider',
            name='slider_img',
            field=models.ImageField(upload_to='slider_imgs', verbose_name='Картинка'),
        ),
    ]
