from django.conf.urls import url

from pages.views import page, insertedpage, PageList

urlpatterns = [
    url(r'^pages/$', PageList.as_view(), name='list'),
    url(r'^(?P<page_title>[\w-]+)/$', page, name='detail'),
    url(r'^(?P<page_title>[\w-]+)/insert/(?P<dropboxpath>.+)/$', insertedpage,
        name='insert-detail'),
]
