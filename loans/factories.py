import factory
from factory.django import DjangoModelFactory
from .models import LoanApplication, Fund, LoanConfiguration
from users.factories import LoanCustomerFactory, LoanProviderFactory

class LoanConfigurationFactory(DjangoModelFactory):
    class Meta:
        model = LoanConfiguration

    max_loan_amount = factory.Faker('pyfloat', right_digits=2, max_value=100000, positive=True)
    min_loan_amount = factory.Faker('pyfloat', right_digits=2, min_value=1000, max_value=50000, positive=True)
    interest_rate = factory.Faker('pydecimal', right_digits=2, max_value=20, positive=True)
    duration = factory.Faker('pyint', min_value=6, max_value=60)

class LoanApplicationFactory(DjangoModelFactory):
    class Meta:
        model = LoanApplication

    provider = factory.SubFactory(LoanProviderFactory)
    customer = factory.SubFactory(LoanCustomerFactory)
    amount = factory.Faker('pydecimal', right_digits=2, max_value=10000, positive=True)
    term_months = factory.Faker('pyint', min_value=1, max_value=120)
    status = factory.Faker('random_element', elements=[choice[0] for choice in LoanApplication.STATUS_CHOICES])
    loan_configuration = factory.SubFactory(LoanConfigurationFactory)
    remaining_amount = factory.Faker('pydecimal', right_digits=2, max_value=10000, positive=True)

class FundFactory(DjangoModelFactory):
    class Meta:
        model = Fund

    provider = factory.SubFactory(LoanProviderFactory)
    amount = factory.Faker('pydecimal', right_digits=2, max_value=10000, positive=True)
    status = factory.Faker('random_element', elements=[choice[0] for choice in Fund.STATUSES])