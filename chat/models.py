from django.db import models


class Message(models.Model):
    body = models.TextField(100)

    def __str__(self):
        return self.body[:40]