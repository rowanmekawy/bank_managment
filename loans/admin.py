from django.contrib import admin
from .models import LoanApplication, Fund, LoanConfiguration

@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'provider', 'customer', 'amount', 'term_months', 'status')
    list_filter = ('provider', 'status')
    search_fields = ('id', 'customer__name')
    ordering = ('-created',)

@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ('id', 'provider', 'amount', 'status')
    list_filter = ('provider', 'status')
    search_fields = ('id',)
    ordering = ('-created',)

@admin.register(LoanConfiguration)
class LoanConfigurationAdmin(admin.ModelAdmin):
    list_display = ('max_loan_amount', 'min_loan_amount', 'interest_rate', 'duration')
