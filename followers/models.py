from django.conf import settings
from django.db import models


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following"
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "followed_user"], name="unique_userfollows"
            )
        ]
        verbose_name_plural = "userfollows"

    def __str__(self):
        return f"{self.user} follows {self.followed_user}"
