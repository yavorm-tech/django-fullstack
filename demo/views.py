# Create your views   here.
from rest_framework import viewsets
from .serializers import FileSerializer
from .models import File
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class FileViewSet(viewsets.ModelViewSet):
    serializer_class =  FileSerializer
    queryset = File.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

