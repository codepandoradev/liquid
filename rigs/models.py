from django.db import models

# Create your models here.

class DetailsType(models.Model):

    type = models.TextField(primary_key=False)


class AvaliableDetail(models.Model):
    type = models.ForeignKey(DetailsType, on_delete=models.CASCADE)
    name = models.TextField()
    
