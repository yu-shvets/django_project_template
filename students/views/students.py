# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.students import Student
from ..models.groups import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.views.generic import UpdateView, DeleteView
from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit


def students_list(request):
    students = Student.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'students_list.html', {'students': students})

def students_add(request):

    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # errors collection
            errors = {}
            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}
            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"День народження є обов'язковим"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                if photo.size > 2 * 1024 * 1024:
                    errors['photo'] = u"Оберіть файл не більше 2 МБ"
                elif photo.name.split('.')[-1] not in ('jpg', 'jpeg', 'png', 'gif'):
                    errors['photo'] = u"Оберіть вірний формат"
                else:
                    data['photo'] = photo

            if not errors:
                student = Student(**data)
                student.save()

                # redirect user to students list
                return HttpResponseRedirect(u'%s?status_message=Cтудента %s %s успішно додано' %
                                            (reverse('home'), first_name, last_name))

            else:
                # render form with errors and previous user input
                return render(request, 'student_add.html',
                    {'groups': Group.objects.all().order_by('title'),
                        'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(u'%s?status_message=Додавання студента скасовано' % reverse('home'))

    else:
        # initial form render
        return render(request, 'student_add.html', {'groups': Group.objects.all().order_by('title')})


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_edit.html'
    fields = '__all__'

    def get_success_url(self):
        return u'%s?status_message=Студента успішно збережено' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редагування студента відмінено!' % reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=Студеннта успішно видалено!' % reverse('home')