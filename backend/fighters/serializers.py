from rest_framework import serializers
from .models import Race, Weapon, Fighter

class WeaponSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Weapon
        fields = '__all__'

class RaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Race
        fields = '__all__'


class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = '__all__'