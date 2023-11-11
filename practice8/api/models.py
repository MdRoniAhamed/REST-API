from django.db import models

CATEGORY = (
    ('male',"Male"),
    ('girl',"Girl")
)

class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,choices=CATEGORY)
    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=300)
    singer = models.ManyToManyField(Singer, related_name='song')
    duration = models.FloatField()

    def __str__(self):
        return self.title