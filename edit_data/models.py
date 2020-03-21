from django.db import models
from django.utils.translation import gettext_lazy as _
from enum import Enum
# Create your models here.

class Sex(models.TextChoices):
    Man = "M", _("Male")
    Women = "F", _("Female")

class Man(models.Model):
    Vorname0 = models.CharField(max_length=256)
    Vorname1 = models.CharField(max_length=256)
    Vorname2 = models.CharField(max_length=256)
    Nachname = models.CharField(max_length=256)
    Sex = models.CharField(max_length=2, choices=Sex.choices)
    Vater = models.CharField(max_length=256)
    Mutter = models.CharField(max_length=256)
    Location_born = models.CharField(max_length=256)
    Location_dead = models.CharField(max_length=256, null=True, blank=True)
    Date_born = models.DateField()
    Date_dead = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.Vorname0

    class Meta:
        verbose_name = "предок"
        verbose_name_plural = "предки"



