
from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовка")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Статус")
    status_name = models.CharField(max_length=100, blank=True, verbose_name="Название статуса")
    remark = models.CharField(max_length=200, blank=True, verbose_name="Ремарки")
    
    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.status_name = self.status.title
        super().save(*args, **kwargs)
        
    
    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name="Название")
    service = models.ManyToManyField(Service)
    
    def __str__(self) -> None:
        return self.name


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"