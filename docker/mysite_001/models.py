from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    publish_date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    clicks = models.TextField()
    summary = models.TextField()
    category = models.TextField()
    class Meta:
        db_table = 'articles'


