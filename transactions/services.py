from .models import LoanPayment
from users.models import LoanCustomer
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

class LoanPaymentServices:
    def create(self, user, amount_paid, loan):
        loan_customer = LoanCustomer.objects.get(user=user.id)
        return LoanPayment.objects.create(
            customer=loan_customer,
            amount_paid=amount_paid,
            loan=loan
        )
    
    def list(self, user):
        if user.role == 'loan_customer':
            loan_applications = LoanPayment.objects.select_related('customer__user').filter(customer__user_id=user.id)
        elif user.role == 'bank_personnel':
            loan_applications = LoanPayment.objects.all()   
        return loan_applications
    
    def details(self, user, id):
        loan_payment = get_object_or_404(LoanPayment, id=id)
        if user.role == 'loan_customer':
            loan_customer = get_object_or_404(LoanCustomer, user=user)
            if loan_payment.customer != loan_customer:
                raise PermissionDenied("You do not have permission to view this loan payment.")
        elif user.role == 'bank_personnel':
            pass
        else:
            raise PermissionDenied("Invalid user role.")
        return loan_payment  