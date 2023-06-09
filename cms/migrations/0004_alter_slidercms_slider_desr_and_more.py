# Generated by Django 4.1.7 on 2023-02-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_slidercms_delete_cmsslider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slidercms',
            name='slider_desr',
            field=models.CharField(max_length=200, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='slidercms',
            name='slider_img',
            field=models.ImageField(upload_to='slider_imgs', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='slidercms',
            name='slider_title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
