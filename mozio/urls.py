from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from providers.views import ProviderViewSet
from service_areas.views import ServiceAreaViewSet
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter(trailing_slash=False)

router.register('providers', ProviderViewSet, basename='providers')
router.register('areas', ServiceAreaViewSet, basename='areas')

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)