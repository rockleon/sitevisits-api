from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, me

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('me/', me, name='me'),
    path('', include(router.urls))
]
