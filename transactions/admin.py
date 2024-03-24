from django.contrib import admin
from .models import LoanPayment
# Register your models here.


@admin.register(LoanPayment)
class LoanPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan', 'amount_paid', 'created', 'modified')
    list_filter = ('loan',)
    search_fields = ('loan__id', 'amount_paid')
    ordering = ('-created',)