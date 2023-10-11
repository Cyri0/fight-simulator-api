from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Fighter, Race, Weapon
from .serializers import FighterSerializer, RaceSerializer, WeaponSerializer

@api_view(['GET'])
def getFighters(request):
    fighters = Fighter.objects.all()
    serialized = FighterSerializer(fighters, many=True)

    return Response(serialized.data)

@api_view(['GET'])
def getRaces(request):
    races = Race.objects.all()
    serialized = RaceSerializer(races, many=True)

    return Response(serialized.data)

@api_view(['GET'])
def getWeapons(request):
    weapons = Weapon.objects.all()
    serialized = WeaponSerializer(weapons, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getWeapon(request, pk):
    try:
        weapon = Weapon.objects.get(id=pk)
    except Exception as e:
        return Response({"message":str(e)})
    serialized = WeaponSerializer(weapon, many=False)
    return Response(serialized.data)

@api_view(['GET'])
def getRace(request, pk):
    try:
        race = Race.objects.get(id=pk)
    except Exception as e:
        return Response({"message":str(e)})
    serialized = RaceSerializer(race, many=False)
    return Response(serialized.data)
