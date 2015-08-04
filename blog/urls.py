from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.reg_form,name='reg_form'),
	url(r'^Post/',views.post_list,name='post_list'),
	url(r'^Post/(?P<pk>[0-9]+)/$',views.post_detail, name='post_detail'),
	url(r'^Form/new/$',	views.reg_form,	name='RegForm'),
]

