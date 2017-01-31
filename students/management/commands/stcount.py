from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from students.models.students import Student, Group


class Command(BaseCommand):
    args = '<model_name model_name ...>'
    help = "Prints to console number of student related objects in a database."

    models = (('student', Student), ('group', Group), ('user', User))

    def add_arguments(self, parser):
        parser.add_argument('student')
        parser.add_argument('group')
        parser.add_argument('user')

    def handle(self, *args, **options):
        student = options['student']
        group = options['group']
        user = options['user']

        for name, model in self.models:
            self.stdout.write('Number of %ss in database: %d' %
                    (name, model.objects.count()))
