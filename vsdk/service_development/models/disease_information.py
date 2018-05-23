from django.db import models
# from django.utils import timezone
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
# from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from .utils import ChoiceEnum

# from . import KasaDakaUser
# from . import VoiceService, VoiceServiceElement
# from . import Language

class disease_info(models.Model):
    class disease_n(ChoiceEnum):
        Newcastle_Disease = "Newcastle Disease"
        Fowl_Pox = "Fowl Pox"
        Bursal_Disease = "Bursal Disease"
        Mareks_Disease = "Marek's Disease"
    disease_name = models.CharField(_('Disease Name'), max_length=200, choices=disease_n.choices(), blank=True, null=True)
    medicine = models.CharField(_('Recommended Medicine'), max_length=200, blank=True, null=True)
    vaccine = models.CharField(_('Recommended Vaccines'), max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = _('Disease Information Database')