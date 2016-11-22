from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

  #  url(r'^', include(ask.qa.urls)),
    url(r'^$','qa.views.test', name='root'),
    url(r'^login/','qa.views.test', name='login'),
    url(r'^new/','qa.views.test', name='new'),
    url(r'^signup/','qa.views.test', name='signup'),
    url(r'^ask/','qa.views.test', name='ask'),
    url(r'^popular/','qa.views.test', name='poplar'),
    url(r'^question/.$','qa.views.test', name='question'),
    url(r'^admin/', include(admin.site.urls)),
)