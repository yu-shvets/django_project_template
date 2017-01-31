# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from ..models.groups import *


class Ex(models.Model):

    class Meta(object):
        verbose_name = u"Іспит"
        verbose_name_plural = u"Іспити"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")

    date_time = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        blank=False,
        verbose_name=u"Дата і час проведення")

    professor_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Ім'я викладача",
        default='')

    ex_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True)

    def __unicode__(self):
        return u"%s %s" % (self.title, self.date_time)