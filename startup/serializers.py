from rest_framework import serializers
from .models import CustomUser, Profession
class CustomUserSerializer(serializers.ModelSerializer):
    profession_name = serializers.CharField(source='profession.name', required=False)
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'full_name', 'profession', 'profession_name', 'fired', 'fired_date', 'user_permissions')
        
class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('id', 'name')
