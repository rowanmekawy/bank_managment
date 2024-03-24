from django.db import models
from django_extensions.db.models import TimeStampedModel
from users.models import LoanProvider, LoanCustomer
# Create your models here.


class LoanConfiguration(TimeStampedModel):
    max_loan_amount = models.FloatField()
    min_loan_amount = models.FloatField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.IntegerField() 

class LoanApplication(TimeStampedModel):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    provider = models.ForeignKey(LoanProvider, on_delete=models.CASCADE, related_name="loan_provider", null=True, blank=True)
    customer = models.ForeignKey(LoanCustomer, on_delete=models.CASCADE, related_name="loan_customer")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    term_months = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    loan_configuration = models.ForeignKey(LoanConfiguration, on_delete=models.CASCADE, related_name="loan_configuration")
    remaining_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)

class Fund(TimeStampedModel):
    STATUSES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected")
    ]
    provider = models.ForeignKey(LoanProvider, on_delete=models.CASCADE, related_name="fund_provider")
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=255, choices=STATUSES, default='pending')

