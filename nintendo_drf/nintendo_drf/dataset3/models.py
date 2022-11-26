from django.db import models

#defining model attributes for specific dataset
class Game(models.Model):
    title = models.CharField(max_length=200)
    cancellation_date = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)

    def __str__(self):
        return self.title