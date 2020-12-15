from rest_framework import serializers
from .models import Contacts


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id',
                  'first_name',
                  'last_name', 'phone',
                  'email')