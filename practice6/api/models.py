from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()
    c_details = models.CharField(max_length=50)
    