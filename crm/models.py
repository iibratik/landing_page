from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=50, verbose_name='Имя статуса')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = ("Статус")
        verbose_name_plural = ("Статусы")


class Order(models.Model):
    order_created = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя клиента')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон клиента')
    order_status = models.ForeignKey(StatusCrm, verbose_name=("Статус"), on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
class ComentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, verbose_name=("Заявка"), on_delete=models.CASCADE)
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateField(auto_now=True, verbose_name='Дата создания коммента')


    class Meta:
        verbose_name = ("Коммент")
        verbose_name_plural = ("Коммент")

    def __str__(self):
        return f"id: {self.pk}, comment: {self.comment_binding}"

    # def get_absolute_url(self):
    #     return reverse(self.pk)


