from django.db import models

class Services(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"


class Orders(models.Model):
    date_of_order = models.DateTimeField()
    services = models.ForeignKey('Services', related_name='orders_services', on_delete=models.CASCADE)
    description = models.TextField(max_length=200, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='orders_user', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_of_order']
        verbose_name = "Запись на приём"
        verbose_name_plural = "Записи на приёмы"