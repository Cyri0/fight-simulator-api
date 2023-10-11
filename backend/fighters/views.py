from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Fighter
from .serializers

def getFighters(request):
    