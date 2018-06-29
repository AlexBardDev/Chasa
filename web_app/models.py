"""
This script contains the models used by 'web_app'.
"""
#Import libraries
from django.db import models

class Places(models.Model):
    """This class contains all about the places."""

    name = models.CharField(max_length=50, verbose_name="Site de plongée")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lieu"
        verbose_name_plural = "Lieux"

class PersonInChargeOf(models.Model):
    """This class contains all the people who can be in charge of a event."""

    name = models.CharField(max_length=50, verbose_name="Personne en charge")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsables"

class DivingEvents(models.Model):
    """This class contains all the data about the diving events."""

    date = models.DateTimeField(verbose_name="Date et heure d'arrivée")
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    person = models.ForeignKey(PersonInChargeOf, on_delete=models.CASCADE)
    extra_infos = models.TextField(verbose_name="Infos supp", null=True, blank=True)

    def __str__(self):
        return """Plongée à {} le {}.""".format(self.place.name, self.date)

    class Meta:
        verbose_name = "Plongée"
        verbose_name_plural = "Plongées"

class ClubEvents(models.Model):
    """This class contains all the data about the club events.
    It's empty for the moment."""

    pass
