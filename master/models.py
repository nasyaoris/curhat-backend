from django.db import models
from django.contrib.auth.model import User

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)s_updated_by', blank=True, null=True)

    class Meta:
        abstract = True
