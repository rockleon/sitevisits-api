from rest_framework.serializers import ModelSerializer
from .models import Account


class AccountSerializers(ModelSerializer):
    class Meta:
      model = Account
      fields = '__all__'