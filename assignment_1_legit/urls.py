from django.conf.urls import patterns, include, url
from django.contrib import admin
from homework import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assignment_1_legit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/(?P<subject>.*)', views.HomeworkList.as_view(), name='homework_list'),
    url(r"^detail/(?P<id>[0-9]+)$", views.details, name = "detail"),
    url(r'^add/$', views.HomeworkCreate.as_view(), name='homework_add'),
    url(r'^homework/(?P<pk>\d+)/edit/$', views.HomeworkUpdate.as_view(),  name='homework_update'),
    url(r'^homework/(?P<pk>\d+)/delete/$', views.HomeworkDelete.as_view(),  name='homework_delete'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^userimg/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'userimg/'}),
    url(r'^$', views.home, name='home')

)
