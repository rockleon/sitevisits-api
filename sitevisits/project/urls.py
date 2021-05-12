from django.urls import include, path
from rest_framework import routers
from .views import ProjectViewSet, IncrementVisits

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('visits/<uuid:key>/', IncrementVisits, name='visits'),
    path('', include(router.urls))
]
