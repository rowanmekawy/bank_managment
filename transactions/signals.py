# -*- coding: utf-8 -*-
import logging
from django.db import transaction, DatabaseError
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import LoanPayment
logger = logging.getLogger("django")

@receiver(post_save, sender=LoanPayment)
def loan_remaining_amount(sender, instance, **kwargs):
    if instance.status == 'approved':
        try:
            with transaction.atomic():
                instance.loan.remaining_amount = instance.loan.amount - instance.amount_paid
                instance.loan.save()
        except DatabaseError as e:
            logger.error(
                "Failed to update remaining amount for LoanPayment id=%s: %s",
                instance.id,
                str(e),
                exc_info=True
            )       