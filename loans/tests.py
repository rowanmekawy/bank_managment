from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .factories import LoanApplicationFactory, FundFactory
from users.factories import UserProfileFactory

# Create your tests here.
@pytest.mark.django_db
class TestLoanApplicationViewSet:
    def setup_method(self):
        self.client = APIClient()
        self.user = UserProfileFactory()
        self.client.force_authenticate(user=self.user)
    
    def test_list_loan_applications(self):
        # Create some loan applications
        LoanApplicationFactory.create_batch(3)
        url = reverse('loan-application-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_retrieve_loan_application(self):
        loan_application = LoanApplicationFactory()
        url = reverse('loan-application-detail', kwargs={'pk': loan_application.id})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == loan_application.id

@pytest.mark.django_db
class TestFundViewSet:
    def setup_method(self):
        self.client = APIClient()
        self.user = UserProfileFactory()
        self.client.force_authenticate(user=self.user)
    
    def test_list_funds(self):
        # Create some funds
        FundFactory.create_batch(3)
        url = reverse('fund-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_retrieve_fund(self):
        fund = FundFactory()
        url = reverse('fund-detail', kwargs={'pk': fund.id})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == fund.id        
