# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Sales(models.Model):

    #__Sales_FIELDS__
    sku = models.CharField(max_length=255, null=True, blank=True)
    total_items_ordered = models.IntegerField(null=True, blank=True)
    platform = models.CharField(max_length=255, null=True, blank=True)

    #__Sales_FIELDS__END

    class Meta:
        verbose_name        = _("Sales")
        verbose_name_plural = _("Sales")


class Flipkart(models.Model):

    #__Flipkart_FIELDS__
    sku = models.CharField(max_length=255, null=True, blank=True)
    external_sku = models.CharField(max_length=255, null=True, blank=True)

    #__Flipkart_FIELDS__END

    class Meta:
        verbose_name        = _("Flipkart")
        verbose_name_plural = _("Flipkart")


class Amazon(models.Model):

    #__Amazon_FIELDS__
    sku = models.CharField(max_length=255, null=True, blank=True)
    external_sku = models.CharField(max_length=255, null=True, blank=True)

    #__Amazon_FIELDS__END

    class Meta:
        verbose_name        = _("Amazon")
        verbose_name_plural = _("Amazon")



#__MODELS__END
