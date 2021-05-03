from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializers import AccountSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Account

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers


@api_view(['GET', 'POST'])
def IncrementVisits(request, key):
    try:
        acc = Account.objects.get(key = key)
    except:
        return Response({"error": "Invalid key!"}, status=400)
    if request.method == 'GET':
        return Response({ "title": acc.title }, status=200)
    if request.method == 'POST':
        acc.visits += 1
        acc.save()
        return Response({ "title": acc.title }, status=200)
    return Response({"error": "Something went wrong!"}, status=400)