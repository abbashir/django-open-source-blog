from django.db import models

SHOW_STATUS = (
    (1, 'Active'),
    (0, 'Inactive'),
)

# Create your models here.


class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    icon_class = models.CharField(max_length=100)
    status = models.SmallIntegerField(choices=SHOW_STATUS)

    def __str__(self):
        return self.name
