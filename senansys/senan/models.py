# coding:utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    """
        用户表
    """
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    iden = models.CharField(max_length=128)

    def __unicode__(self):
        return self.username

