from rest_framework import serializers
from.models import *


class coin_detail(serializers.ModelSerializer):
    class Meta:
        model = currency_model
        fields = '__all__'