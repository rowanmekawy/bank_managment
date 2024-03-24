# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import LoanPayment

@receiver(post_save, sender=LoanPayment)
def loan_remaining_amount(sender, instance, **kwargs):
    if instance.status == 'approved':
        instance.loan.remaining_amount = instance.loan.amount - instance.amount_paid
        instance.loan.save()