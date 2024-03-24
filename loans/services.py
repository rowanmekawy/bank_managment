from .models import LoanApplication, Fund
from users.models import LoanProvider, LoanCustomer
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

class LoanApplicationServices:
    def create(self, user, amount, loan_configuration, term_months):
        loan_customer, created = LoanCustomer.objects.get_or_create(user=user)
        return LoanApplication.objects.create(
            customer=loan_customer,
            amount=amount,
            loan_configuration=loan_configuration,
            term_months=term_months
        )
    
    def list(self, user):
        if user.role == 'loan_provider':
            loan_applications = LoanApplication.objects.select_related('provider__user').filter(provider__user_id=user.id)
        elif user.role == 'loan_customer':
            loan_applications = LoanApplication.objects.select_related('customer__user').filter(customer__user_id=user.id)
        elif user.role == 'bank_personnel':
            loan_applications = LoanApplication.objects.all()   
        return loan_applications
    
    def details(self, user, id):
        loan_application = get_object_or_404(LoanApplication, id=id)  
        if user.role == 'loan_provider':
            loan_provider = get_object_or_404(LoanProvider, user=user)
            if loan_application.provider != loan_provider:
                raise PermissionDenied("You do not have permission to view this loan application.")
        elif user.role == 'loan_customer':
            loan_customer = get_object_or_404(LoanCustomer, user=user)
            if loan_application.customer != loan_customer:
                raise PermissionDenied("You do not have permission to view this loan application.")
        elif user.role == 'bank_personnel':
            pass
        else:
            raise PermissionDenied("Invalid user role.")
        return loan_application
    
class FundServices:
    def create(self, user, amount):
        provider, created = LoanProvider.objects.get_or_create(user=user)
        return Fund.objects.create(
            provider=provider,
            amount=amount,
        )    