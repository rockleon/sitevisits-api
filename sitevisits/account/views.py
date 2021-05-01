from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializers import AccountSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Account

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers


@api_view(['POST'])
def IncrementVisits(request, key):
    if request.method == 'POST':
        acc = Account.objects.get(key = key)
        acc.visits += 1
        acc.save()
        return Response({ "title": acc.title, "key": key, "visits": acc.visits})
    return Response({"error": "Something went wrong"})