import logging
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from users.permissions import IsBankPersonnelOrLoanCustomer, IsBankPersonnel, IsBankPersonnelOrLoanProvider
from .serializers import LoanApplicationSerializer, FundSerializer, FundCreateSerializer, LoanApplicationCreateSerializer
from .services import LoanApplicationServices, FundServices
from .models import LoanApplication, Fund

logger = logging.getLogger("django")

class LoanApplicationViewSet(viewsets.ModelViewSet):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_serializer_class(self):
        if self.action == 'create':
            return LoanApplicationCreateSerializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        try:
            loan_applications = LoanApplicationServices().list(user=request.user)
        except Exception as e:
            logger.error("Failed to list loan applications for user %s: %s", request.user, str(e))
            return Response({"error": str(e)}, status=400)
        serializer = self.get_serializer(loan_applications, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            loan_application = LoanApplicationServices().details(user=request.user, id=kwargs.get('pk'))
        except Exception as e:
            logger.error("Failed to retrieve loan application %s for user %s: %s", kwargs.get('pk'), request.user, str(e))
            return Response({"error": str(e)}, status=400)
        serializer = self.get_serializer(loan_application)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated, IsBankPersonnelOrLoanCustomer]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            LoanApplicationServices().create(user=request.user, **serializer.validated_data)
        except Exception as e:
            logger.error("Failed to create loan application for user %s: %s", request.user, str(e))
            return Response({"error": str(e)}, status=400)
        return Response({"message": "Loan Application created successfully"}, status=status.HTTP_201_CREATED)  

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated, IsBankPersonnel]
        self.check_permissions(request)
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            logger.error("Failed to update loan application %s for user %s: %s", kwargs.get('pk'), request.user, str(e))
            return Response({"error": str(e)}, status=400)


    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated, IsBankPersonnel]
        self.check_permissions(request)
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            logger.error("Failed to delete loan application %s for user %s: %s", kwargs.get('pk'), request.user, str(e))
            return Response({"error": str(e)}, status=400)
    
class FundViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer    
    permission_classes = [permissions.IsAuthenticated, IsBankPersonnelOrLoanProvider]

    def get_serializer_class(self):
        if self.action == 'create':
            return FundCreateSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            FundServices().create(user=request.user, **serializer.validated_data)
        except Exception as e:
            logger.error("Failed to create fund for user %s: %s", request.user, str(e))
            return Response({"error": str(e)}, status=400)
        return Response({"message": "Loan Application created successfully"}, status=status.HTTP_201_CREATED)  

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated, IsBankPersonnel]
        self.check_permissions(request)
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            logger.error("Failed to update fund %s for user %s: %s", kwargs.get('pk'), request.user, str(e))
            return Response({"error": str(e)}, status=400)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated, IsBankPersonnel]
        self.check_permissions(request)
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            logger.error("Failed to delete fund %s for user %s: %s", kwargs.get('pk'), request.user, str(e))
            return Response({"error": str(e)}, status=400)