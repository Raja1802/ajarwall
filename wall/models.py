from django.db import models
from datetime import datetime


class HomePage(models.Model):
    class Meta:
        db_table = 'homepage'
    image_name = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.CharField(max_length=1000, blank=True, null=True)
    time_added = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.image_name


class WallImage(models.Model):
    class Meta:
        db_table = 'wallimage'
    image_type = models.CharField(max_length=100, blank=True, null=True)
    image_tags = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.CharField(max_length=100, blank=True, null=True)
    image_thumb = models.CharField(max_length=100, blank=True, null=True)
    time_added = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.image_type


class Catlog(models.Model):
    class Meta:
        db_table = 'catlog'
    catlog_thumb = models.CharField(max_length=100, blank=True, null=True)
    catlog_name = models.CharField(max_length=20, blank=True, null=True)
    catlog_keyword = models.CharField(max_length=20, blank=True, null=True)
    catlog_created_time = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.catlog_name

