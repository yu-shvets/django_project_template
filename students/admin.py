 # -*- coding: utf-8 -*-

from django.contrib import admin
from .models.students import Student, Group
from .models.monthjournal import MonthJournal
from .models.exams import Ex
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

# Register your models here.


class StudentFormAdmin(ModelForm):

    def clean_student_group(self):
        # get group where current student is a leader
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(u'Студент є старостою іншої групи.', code='invalid')

        return self.cleaned_data['student_group']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']

    form = StudentFormAdmin

    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk': obj.id})


admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
admin.site.register(Ex)
admin.site.register(MonthJournal)