from django.db import models

#defining model attributes for specific dataset
class Game(models.Model):
    title = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    publisher1 = models.CharField(max_length=200)
    publisher2 = models.CharField(max_length=200)
    release_date1 = models.CharField(max_length=200)
    release_date2 = models.CharField(max_length=200)

    def __str__(self):
        return self.title