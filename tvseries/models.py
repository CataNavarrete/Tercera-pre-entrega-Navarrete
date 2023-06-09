from django.db import models

class TVSeries(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.title
