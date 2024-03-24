# -*- coding: utf-8 -*-
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import LoanApplication, Fund
from django.core.exceptions import ValidationError

@receiver(post_save, sender=LoanApplication)
def validate_total_funds(sender, instance, **kwargs):
    max_amount = instance.loan_configuration.max_loan_amount
    min_amount = instance.loan_configuration.min_loan_amount
    if instance.amount > max_amount or instance.amount < min_amount:
            raise ValidationError("The total loan amount is not in the correct range.")
    if instance.status == 'approved':
        total_loans = LoanApplication.objects.filter(
            status='approved'
        ).aggregate(
            total=Sum('remaining_amount')
        )['total'] or 0
        total_funds = Fund.objects.filter(
            status='approved', provider=instance.provider
        ).aggregate(
            total=Sum('amount')
        )['total'] or 0
        if total_loans + instance.amount > total_funds:
            raise ValidationError("The total loan amount cannot exceed the total available funds.")