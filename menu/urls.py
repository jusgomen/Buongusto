from django.conf.urls import url
from django.contrib.auth.views import login
from django.views.generic import *

from . import views
from menu.views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^menu/', views.menu, name='menu'),

    url(r'^signin/', views.signin, name='signin'),
    url(r'^login/', views.login, {}),
    url(r'^bookings/', views.bookings,{}),
    url(r'^tables/', views.tables, name='tables'),
    
    url(r'^thanks/', views.thanks, {}),


    url(r'^waiter/', views.waiter, {}),
    url(r'^waiterList/$', OrderView.as_view(),name='add-order'),
    url(r'^waiterList2/$', CustomerView.as_view(),name='add-customer'),


    url(r'^cook/', views.cook, {}),
    url(r'^boss/', views.boss, {}),

    url(r'^waiter/create$', views.create, name='create'),
    url(r'^waiter/read$', views.read, name='read'),
    url(r'^waiter/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^waiter/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^waiter/delete/(?P<id>\d+)$', views.delete, name='delete'),
]
