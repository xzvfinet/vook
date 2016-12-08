from __future__ import unicode_literals

from django.db import models


class Page(models.Model):
    next_page = models.ForeignKey('Page', blank=True, null=True)

    index = models.IntegerField()
    image_file = models.ImageField(upload_to='uploaded/original/%Y/%m/%d')

    click_count = models.IntegerField(default=0)
    limit = models.IntegerField(default=0)

    def delete(self, *args, **kwargs):
        self.image_file.delete()

    def click(self):
        if self.click_count >= self.limit:
            return False
        self.click_count += 1
        return True

    def reset(self):
        self.click_count = 0



