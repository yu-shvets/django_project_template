# -*- coding: utf-8 -*-

from django.shortcuts import render
from ..models.exams import Ex
from ..util import get_current_group


def exams_list(request):
    current_group = get_current_group(request)

    if current_group:
        exams = Ex.objects.filter(ex_group=current_group)
    else:
        exams = Ex.objects.all()

    order_by = request.GET.get('order_by', '-date')
    if order_by in ('date_time'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '-date') == '1':
            exams = exams.reverse()

    return render(request, 'exams.html', {'exams': exams})