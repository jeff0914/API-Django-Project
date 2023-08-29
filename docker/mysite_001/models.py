from django.db import models
import uuid

# Create your models here.
class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    publish_date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    clicks = models.IntegerField()
    summary = models.TextField()
    category = models.TextField()
    class Meta:
        db_table = 'articles'


