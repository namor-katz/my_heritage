from django.db import models
from django.utils.translation import gettext_lazy as _
from enum import Enum
# Create your models here.

##utilites class
class Sex(models.TextChoices):
    Man = "M", _("Male")
    Women = "F", _("Female")


class Day(models.TextChoices):
    M = "M",  _("Monday")
    T = "T",  _("Tuesday")
    W = "W",  _("Wednesday")
    TU = "TU",  _("Thursday")
    F = "F",  _("Friday")
    S = "S",  _("Saturday")
    SU = "SU",  _("Sunday")


class Role(models.TextChoices):
    Self = "S", _("Self")
    Vater = "V", _("Vater")
    Mutter = "M", _("Mutter")
    Ehemann = "E", _("Ehemann")
    Ehefrau = "F", _("Frau")


class EventType(models.TextChoices):
    Born = "B", _("geBorn")
    Taufen = "T", _("geTaufen")
    Heiraten = "H", _("verHeiratet")
    Sterben = "S",  _("Sterben")


## base models class
class Man(models.Model):
    Vorname0 = models.CharField(max_length=256)
    Vorname1 = models.CharField(max_length=256, null=True, blank=True)
    Vorname2 = models.CharField(max_length=256, null=True, blank=True)
    Nachname = models.CharField(max_length=256)
    Sex = models.CharField(max_length=2, choices=Sex.choices)

    def __str__(self):
        return self.Vorname0

    class Meta:
        verbose_name = "предок"
        verbose_name_plural = "предки"


class Event(models.Model):
    member0 = models.ForeignKey(Man, related_name="member0", verbose_name="Member0", on_delete=models.PROTECT)
    role0 = models.CharField(max_length=1, choices=Role.choices)
    member1 = models.ForeignKey("Man", on_delete=models.PROTECT, related_name="member1", verbose_name="Member1", null=True, blank=True)
    role1 = models.CharField(max_length=1, choices=Role.choices, null=True, blank=True)
    member2 = models.ForeignKey("Man", on_delete=models.PROTECT, related_name="member2", verbose_name="Member2", null=True, blank=True)
    role2 = models.CharField(max_length=1, choices=Role.choices, null=True, blank=True)
    date = models.DateField()
    type = models.CharField(max_length=2, choices=EventType.choices)
    day = models.CharField(max_length=2, choices=Day.choices)
    locations = models.CharField(max_length=256)

    class Meta:
        verbose_name = "событие"
        verbose_name_plural = "события"

    def __str__(self):
        return self.type