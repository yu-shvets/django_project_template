# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from ..models.students import Student


class MonthJournal(models.Model):

    class Meta:
        verbose_name = u'Місячний Журнал'
        verbose_name_plural = u'Місячні Журнали'

    student = models.ForeignKey('Student',
        verbose_name=u'Студент',
        blank=False,
        unique_for_month='date')

    date = models.DateField(
        verbose_name=u'Дата',
        blank=False)

    present_day1 = models.BooleanField(default=False)
    present_day2 = models.BooleanField(default=False)
    present_day3 = models.BooleanField(default=False)
    present_day4 = models.BooleanField(default=False)
    present_day5 = models.BooleanField(default=False)
    present_day6 = models.BooleanField(default=False)
    present_day7 = models.BooleanField(default=False)
    present_day8 = models.BooleanField(default=False)
    present_day9 = models.BooleanField(default=False)
    present_day10 = models.BooleanField(default=False)
    present_day11 = models.BooleanField(default=False)
    present_day12 = models.BooleanField(default=False)
    present_day13 = models.BooleanField(default=False)
    present_day14 = models.BooleanField(default=False)
    present_day15 = models.BooleanField(default=False)
    present_day16 = models.BooleanField(default=False)
    present_day17 = models.BooleanField(default=False)
    present_day18 = models.BooleanField(default=False)
    present_day19 = models.BooleanField(default=False)
    present_day20 = models.BooleanField(default=False)
    present_day21 = models.BooleanField(default=False)
    present_day22 = models.BooleanField(default=False)
    present_day23 = models.BooleanField(default=False)
    present_day24 = models.BooleanField(default=False)
    present_day25 = models.BooleanField(default=False)
    present_day26 = models.BooleanField(default=False)
    present_day27 = models.BooleanField(default=False)
    present_day28 = models.BooleanField(default=False)
    present_day29 = models.BooleanField(default=False)
    present_day30 = models.BooleanField(default=False)
    present_day31 = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s: %d, %d' % (self.student.last_name, self.date.month, self.date.year)


'''attributes = [('present_day' + str(i), models.BooleanField(default=False)) for i in range(1, 32)]

for key, value in attributes:
    setattr(MonthJournal, key, value)'''
