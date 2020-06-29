from django.db import models
from django.utils import timezone

# Create your models here.
class File(models.Model):
    filename = models.CharField(max_length=64, default="")
    sha256 = models.CharField(max_length=128, default="")
    filesize = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)
    mimetype = models.CharField(max_length=36, default="")
    date_submitted = models.DateTimeField(blank=False,default=timezone.now())
    date_finnished = models.DateTimeField(blank=False, default=timezone.now())

    def __str__(self):
        return self.filename