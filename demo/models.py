from django.db import models
from django.utils import timezone


class FileMetadata(models.Model):
    encrypted = models.BooleanField(default=False)
    file_abs_path = models.TextField(max_length=64, null=False, blank=False, default="")

# Create your models here.
class File(models.Model):
    filename = models.CharField(max_length=64, default="")
    sha256 = models.CharField(max_length=128, default="")
    filesize = models.IntegerField(null=False, default=0)
    mimetype = models.CharField(max_length=36, default="")
    date_submitted = models.DateTimeField(blank=False,default=timezone.now())
    date_finnished = models.DateTimeField(blank=False, default=timezone.now())
    metadata = models.OneToOneField(FileMetadata, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.filename

class Evaluation(models.Model):
    uuid = models.CharField(max_length=128, null=False, default="")
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='evaluations')

class Client(models.Model):
    name = models.CharField(max_length=128, null=False, default="");
    certificate_metadata = models.TextField(max_length=128, null=False, default="")
    ip_address = models.GenericIPAddressField(null=False, default="0.0.0.0")
    evaluations = models.ManyToManyField(File)

