# -*- coding: utf-8 -*-

from django.shortcuts import render


def journal(request):
    return render(request, 'journal.html', {})