"""bank_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from loans.views import LoanApplicationViewSet, FundViewSet, LoanConfigurationList
from transactions.views import LoanPaymentViewSet
from users.views import UserProfileListCreate
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register(r'loan-applications', LoanApplicationViewSet, basename='loan-application')
router.register(r'funds', FundViewSet, basename='fund')
router.register(r'loan-payment', LoanPaymentViewSet, basename='loan-payment')
router.register(r'loan-configuration', LoanConfigurationList, basename='loan-configuration')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/token/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path("schema/swagger-ui/", login_required(SpectacularSwaggerView.as_view(url_name="schema")), name="swagger-ui"),
    path('schema/redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('users/', UserProfileListCreate.as_view(), name='user-list-create'),
    path('', include(router.urls)),

]
