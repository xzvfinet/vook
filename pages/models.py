from __future__ import unicode_literals

from django.db import models


class Page(models.Model):
    next_page = models.ForeignKey('Page', blank=True, null=True)

    index = models.IntegerField()
    image_file = models.ImageField(upload_to='uploaded/original/%Y/%m/%d')

    def delete(self, *args, **kwargs):
        self.image_file.delete()


