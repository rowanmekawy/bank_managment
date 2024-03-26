import logging
from rest_framework import status, viewsets
from rest_framework.response import Response
from users.permissions import IsBankPersonnelOrLoanCustomer, IsBankPersonnel
from .models import LoanPayment
from .serializers import LoanPaymentCreateSerializer, LoanPaymentSerializer
from .services import LoanPaymentServices

logger = logging.getLogger("django")
# Create your views here.
class LoanPaymentViewSet(viewsets.ModelViewSet):
    queryset = LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer
    permission_classes = [IsBankPersonnelOrLoanCustomer]

    def get_serializer_class(self):
        if self.action == 'create':
            return LoanPaymentCreateSerializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        try:
            loan_applications = LoanPaymentServices().list(user=request.user)
        except Exception as e:
            logger.error("Failed to list loan payments for user %s: %s", request.user, str(e))
            return Response({"error": str(e)}, status=400)
        serializer = self.get_serializer(loan_applications, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            loan_application = LoanPaymentServices().details(user=request.user, id=kwargs.get('pk'))
        except Exception as e:
            logger.error("Failed to retrieve loan payment %s for user %s: %s", kwargs.get('pk'), request.user, str(e))
            return Response({"error": str(e)}, status=400)
        serializer = self.get_serializer(loan_application)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            LoanPaymentServices().create(user=request.user, **serializer.validated_data)
        except Exception as e:
            logger.error("Failed to create loan payment for user %s: %s", request.user, str(e))
            return Response({"error": str(e)}, status=400)
        return Response({"message": "Loan Application created successfully"}, status=status.HTTP_201_CREATED)  

    def update(self, request, *args, **kwargs):
        self.permission_classes = [IsBankPersonnel]
        self.check_permissions(request)
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            logger.error("Failed to update loan payment %s for user %s: %s", kwargs.get('pk'), request.user, str(e))
            return Response({"error": str(e)}, status=400)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [IsBankPersonnel]
        self.check_permissions(request)
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            logger.error("Failed to delete loan payment %s for user %s: %s", kwargs.get('pk'), request.user, str(e))
            return Response({"error": str(e)}, status=400) 