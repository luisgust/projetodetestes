from django.conf.urls import patterns, include, url
from django.contrib import admin
from matricula import views
from matricula import urls

urlpatterns = patterns('',
    # Examples:
     url(r'^$', views.home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^matricula/', include('matricula.urls')),
)
