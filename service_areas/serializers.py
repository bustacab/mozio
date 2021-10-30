from .models import ServiceArea
from rest_framework.serializers import ModelSerializer


class ServiceAreaSerializer(ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = "__all__"
