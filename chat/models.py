from django.db import models


class Message(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.name + ' : ' + self.body[:40]