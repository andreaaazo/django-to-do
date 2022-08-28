from django.db import models
from django.utils.timezone import now

# Create your models here.
class Thing(models.Model):
    body = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(("Date"), default=now)

    def __str__(self) -> str:
        return self.body
