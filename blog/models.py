from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title
