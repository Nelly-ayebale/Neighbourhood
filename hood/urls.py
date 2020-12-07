from django.urls import path
from . import views
from .views import index,HoodSetView,BusinessSetView,PostSetView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r"hood",HoodSetView)
router.register(r"business",BusinessSetView)
router.register(r"posts",PostSetView)

urlpatterns=[
    path('',views.index,name='index'),
    path('userlist/', views.UserListView.as_view()),
] + router.urls

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
