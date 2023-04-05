from django.conf import settings
from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=128, null=True)
    description = models.TextField(max_length=2048, blank=True, null=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
