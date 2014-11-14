from django.conf.urls import patterns, url
from trivia import views

urlpatterns = patterns('', 

	url(r'^$', views.index, name = 'index'),
	url(r'^(?P<q_id>\d+)/$', views.FCdetail, name = 'FCdetail'),
	url(r'^(?P<q_id>\d+)/FCanswer/$', views.FCanswer, name = 'FCanswer'),
)