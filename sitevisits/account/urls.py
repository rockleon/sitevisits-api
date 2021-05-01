from django.urls import include, path
from rest_framework import routers
from .views import AccountViewSet, IncrementVisits

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet, basename='accounts')

urlpatterns = [
    path('visits/<uuid:key>/', IncrementVisits, name='visits'),
    path('', include(router.urls))
]
