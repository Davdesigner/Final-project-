from django.shortcuts import get_object_or_404
from .models import Location
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import LocationSerializer

class LocationList(APIView):
    def get(self, request):
        locations = Location.objects.all()[:100]
        data = LocationSerializer(locations, many=True).data
        return Response(data)
    
class LocationDetail(APIView):
    def get(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        data = LocationSerializer(location).data
        return Response(data)