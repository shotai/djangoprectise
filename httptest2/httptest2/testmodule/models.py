from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TestModule(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    testmodule_id = models.IntegerField()
    status = models.BooleanField()
    class Meta:
        ordering=('created',)
