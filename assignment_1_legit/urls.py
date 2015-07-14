from django.conf.urls import patterns, include, url
from django.contrib import admin
from homework import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assignment_1_legit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.listing),
    url(r"^detail/(?P<hw_id>[0-9]+)$", views.details, name = "detail"),
)
