import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from .models import LoanProvider, LoanCustomer

class UserProfileFactory(DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker('user_name')
    password = factory.Faker('password')

class LoanProviderFactory(DjangoModelFactory):
    class Meta:
        model = LoanProvider

    user = factory.SubFactory(UserProfileFactory)
    total_budget = factory.Faker('pydecimal', right_digits=2, max_value=1000000, positive=True)

class LoanCustomerFactory(DjangoModelFactory):
    class Meta:
        model = LoanCustomer

    user = factory.SubFactory(UserProfileFactory)
    credit_score = factory.Faker('pyint', min_value=300, max_value=850)
