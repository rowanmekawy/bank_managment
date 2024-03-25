
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, Group, Permission, PermissionsMixin
from .managers import UserProfileManager
# Create your models here.


class UserProfile(AbstractBaseUser, PermissionsMixin):
    USER_ROLES = (
        ('loan_provider', 'Loan Provider'),
        ('loan_customer', 'Loan Customer'),
        ('bank_personnel', 'Bank Personnel'),
    )
    role = models.CharField(max_length=20, choices=USER_ROLES)
    username =  models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="user_profile_set",
        related_query_name="user_profile",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="user_profile_set",
        related_query_name="user_profile",
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
class BankPersonnel(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='bank_personnel')
    position = models.CharField(max_length=255)   

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.pk is not None:
            super().save(*args, **kwargs)
            return
        if self.user.role != 'bank_personnel':
            raise ValidationError("user does not have the required role")
        super().save(*args, **kwargs) 
    
class LoanProvider(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='loan_provider')
    total_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)  

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.pk is not None:
            super().save(*args, **kwargs)
            return
        if self.user.role != 'loan_provider':
            raise ValidationError("user does not have the required role")
        super().save(*args, **kwargs) 

class LoanCustomer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='loan_customer')
    credit_score = models.IntegerField(default=0)    

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.pk is not None:
            super().save(*args, **kwargs)
            return
        if self.user.role != 'loan_customer':
            raise ValidationError("user does not have the required role")
        super().save(*args, **kwargs) 

