"""django_project_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from students.views import students, groups, journal, exams, contact_admin
from .settings import MEDIA_ROOT, DEBUG
from django.conf import settings
from django.views.static import serve
from django.views.i18n import javascript_catalog
from django.views.i18n import JavaScriptCatalog
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # Students urls
    url(r'^$', students.students_list, name='home'),
    url(r'^students/add/$', students.students_add, name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', students.StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', students.StudentDeleteView.as_view(), name='students_delete'),

    # Groups urls
    url(r'^groups/$', groups.groups_list, name='groups'),
    url(r'^groups/add/$', login_required(groups.groups_add), name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups.groups_delete, name='groups_delete'),

    # Journal urls
    url(r'^journal/(?P<pk>\d+)?/?$', journal.JournalView.as_view(), name='journal'),

    # Exams urls
    url(r'^exams/$', exams.exams_list, name='exams'),

    # Contact_admin url
    url(r'^contact-admin/$', contact_admin.contact_admin, name='contact_admin'),

    url(r'^jsi18n\.js$', JavaScriptCatalog.as_view(packages=['students']), name='javascript-catalog'),

    url(r'^admin/', include(admin.site.urls)),

    # User Related urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(
        template_name='registration/profile.html')), name='profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'},
        name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),
        name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),

    # Social Auth Related urls
    url('^social/', include('social_django.urls', namespace='social')),
    ]

if settings.DEBUG:
# serve files from media folder
        urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
                        ]



