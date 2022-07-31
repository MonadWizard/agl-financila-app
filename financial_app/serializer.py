from rest_framework import serializers
from .models import UserFinancialdata

class UserFinancialdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFinancialdata
        fields = ["user_id", "clerk_file"]
