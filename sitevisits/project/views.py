from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Project

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Project.objects.all()
        else:
            return Project.objects.filter(author=self.request.user)


@api_view(['GET', 'POST'])
def IncrementVisits(request, key):
    try:
        acc = Project.objects.get(key = key)
    except:
        return Response({"error": "Invalid key!"}, status=400)
    if request.method == 'GET':
        return Response({ "title": acc.title }, status=200)
    if request.method == 'POST':
        acc.visits += 1
        acc.save()
        return Response({ "title": acc.title }, status=200)
    return Response({"error": "Something went wrong!"}, status=400)