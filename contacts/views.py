from django.shortcuts import render
from .models import Contacts
from .serializers import ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins

# Create your views here.
def home(request):
    
    return render(request, 'index.html')



class ContactListView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer



class ContactUpdateAPIView(generics.UpdateAPIView,
                            mixins.ListModelMixin,
                            mixins.UpdateModelMixin):

    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)  # performs the update operation
        return self.list(request, *args, **kwargs)