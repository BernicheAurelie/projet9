from django.conf import settings
from django.db import models


# Create your models here.
class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        unique_together = ('user', 'followed_user')
        verbose_name_plural = "userfollows"

    def __str__(self):
        return f"{self.user} follows {self.followed_user}"