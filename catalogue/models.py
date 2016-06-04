from __future__ import unicode_literals

from django.db import models

# def cat_images_upload_location(instance, filename):
#     return "%s/%s" %(instance.id, filename)

# Create your models here.
class CatalogueImages(models.Model):
    title = models.CharField(max_length = 20)
    image = models.ImageField(upload_to="images/catalogue")
    desc = models.CharField(max_length = 100,
                            null=True,
                            blank=True)

    def __unicode__(self):
        return self.title
