# -*- coding: utf-8 -*-
from rest_framework import serializers

from . import models


class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoanPayment
        fields = "__all__"

class LoanPaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoanPayment
        exclude = ('status','customer')             