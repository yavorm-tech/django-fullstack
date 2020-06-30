from rest_framework import serializers
from .models import  File, FileMetadata, Evaluation, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','name', 'evaluations']
class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ['uuid', 'file']
class FileMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileMetadata
        fields = ['file_abs_path', 'encrypted']

class FileSerializer(serializers.ModelSerializer):
    metadata = FileMetadataSerializer(many=False)
    evaluations = EvaluationSerializer(many=True)
    clients = ClientSerializer(many=True)
    class Meta:
        model = File;
        fields = ['filename', 'sha256', 'mimetype', 'metadata', 'evaluations', 'clients']

