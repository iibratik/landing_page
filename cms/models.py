from django.db import models

# Create your models here.
class SliderCms(models.Model):
    slider_img = models.ImageField(upload_to='slider_imgs', verbose_name='Картинка')
    slider_title = models.CharField(max_length=200,verbose_name='Заголовок')
    slider_desr = models.CharField(max_length=200, verbose_name='Описание')
    slider_css = models.CharField(max_length=20,null=True, default='-', verbose_name='Активный слайд')

    def __str__(self):
        return self.slider_title

    class Meta:
        verbose_name='Слайд'
        verbose_name_plural = 'Слайды'