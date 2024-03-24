# -*- coding: utf-8 -*-
from rest_framework import serializers

from . import models


class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoanApplication
        fields = "__all__"

class LoanApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoanApplication
        exclude = ('status','provider','remaining_amount','customer')         

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fund
        fields = '__all__'

class FundCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fund
        exclude = ('status','provider')      