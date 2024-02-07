from django.db import models
from djongo.models import ObjectIdField

# Create your models here.
class Article(models.Model):
    id = ObjectIdField()
    title = models.TextField()
    content = models.TextField()