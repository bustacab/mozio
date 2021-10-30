from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ServiceAreaSerializer
from .models import ServiceArea


class ServiceAreaViewSet(ModelViewSet):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()

    @action(methods=["POST"], url_path='search', detail=False)
    def search_place(self, request):
        lat, long = request.data.values()
        return Response({"lat": lat, "long": long})
