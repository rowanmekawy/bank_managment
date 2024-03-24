from django.contrib import admin
from .models import BankPersonnel, LoanProvider, LoanCustomer, UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ("id", "role")
    list_filter = ("role",)
    search_fields = ["id", ]

@admin.register(BankPersonnel)
class BankPersonnelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position')

@admin.register(LoanProvider)
class LoanProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_budget')

@admin.register(LoanCustomer)
class LoanCustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'credit_score')    