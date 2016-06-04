from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FeedBack(models.Model):
    TYPE_CHOICES = (
        ('COMPLAINT', 'Complaint'),
        ('COMPLEMENT','Complement'),
        ('OTHER','Other'),
    )
    fullname = models.CharField(max_length = 120)
    contactNo = models.CharField(max_length = 20)
    emailAddr = models.EmailField()
    type = models.CharField(max_length = 20,
                            choices=TYPE_CHOICES,
                            default='OTHER')
    message = models.TextField (max_length = 1000)
    timeStamp = models.DateTimeField(auto_now=False,
                                    auto_now_add=True)

    def __unicode__(self):
        return self.fullname
