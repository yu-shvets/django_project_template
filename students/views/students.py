# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Міккі',
         'last_name': u'Миша',
         'ticket': 2123,
         'image': 'img/Mickey.jpg'},
        {'id': 2,
         'first_name': u'Дональд',
         'last_name': u'Качка',
         'ticket': 2124,
         'image': 'img/Donald.jpg'},
        {'id': 3,
         'first_name': u'Плутон',
         'last_name': u'Пес',
         'ticket': 2125,
         'image': 'img/Pluto.jpg'},
    )
    return render(request, 'students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)