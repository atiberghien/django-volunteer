from django.conf.urls import patterns, include, url

from django.contrib import admin
from volunteer.base.views import AddVolunteerView, CalendarView, UpdateVolunteerView
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'volunteer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^calendar/', CalendarView.as_view(), name='volunteer-calendar'),
    url(r'^update/(?P<pk>\d+)/$', UpdateVolunteerView.as_view(), name='volunteer-update'),
    url(r'^', AddVolunteerView.as_view(), name='volunteer-index'),
)
