from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default='Other', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Link(models.Model):
    url = models.CharField(max_length=255, blank=False, null=True, unique=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.url
