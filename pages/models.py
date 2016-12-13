from __future__ import unicode_literals

from django.db import models


class Page(models.Model):
    index = models.IntegerField()

    next_page = models.ForeignKey('Page', blank=True, null=True)

    image_file = models.ImageField(upload_to='uploaded/original/%Y/%m/%d')

    click_count = models.IntegerField(default=0)
    limit = models.IntegerField(default=0)

    def __unicode__(self):
        return 'Page: ' + str(self.id)

    def delete(self, *args, **kwargs):
        self.image_file.delete()
        super(Page, self).delete(*args, **kwargs)

    def click(self):
        if self.click_count >= self.limit:
            return True
        self.click_count += 1
        return False

    def reset(self):
        self.click_count = 0



