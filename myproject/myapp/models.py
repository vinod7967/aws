from django.db import models
class Blog(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateField()
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.title
# Create your models here.
