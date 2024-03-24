from django.db import models
from django_extensions.db.models import TimeStampedModel
from users.models import LoanCustomer
from loans.models import LoanApplication

# Create your models here.
class LoanPayment(TimeStampedModel):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    customer = models.ForeignKey(LoanCustomer, on_delete=models.CASCADE, related_name="loan_customer_payment")
    loan = models.ForeignKey(LoanApplication, on_delete=models.CASCADE, related_name="loan")
    amount_paid = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')