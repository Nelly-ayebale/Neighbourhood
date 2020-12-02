from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import index,NeighbourhoodViewSet,ProfileViewSet,BusinessViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"hood",NeighbourhoodViewSet)
router.register(r"profile",ProfileViewSet)
router.register(r"business",BusinessViewSet)

urlpatterns=[
    path('',views.index,name='index')] + router.urls

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)