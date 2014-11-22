from django.conf.urls import patterns, url
from trivia import views

urlpatterns = patterns('', 

	url(r'^$', views.home, name = 'home'),
	
	url(r'^(?P<category>[A-z]\w+ [A-z]\w+)/(?P<q_id>\d+)/answer/$', views.FCanswer, name = 'FCanswer'),
	url(r'^(?P<category>[A-z]\w+)/(?P<q_id>\d+)/answer/$', views.FCanswer, name = 'FCanswer'),
	
	url(r'^about/$', views.about, name = 'about'),
	url(r'^tags/$', views.chooseTag, name = 'tags'),
	url(r'^mode/$', views.mode, name = 'mode'),
	
	url(r'^(?P<category>[A-z]\w+ [A-z]\w+)/$', views.randomFC, name = 'randomFC'),
	url(r'^(?P<category>[A-z]\w+)/$', views.randomFC, name = 'randomFC'),
	
	url(r'^(?P<category>[A-z]\w+ [A-z]\w+)/(?P<q_id>\d+)/$', views.returnFC, name = 'returnFC'),
	url(r'^(?P<category>[A-z]\w+)/(?P<q_id>\d+)/$', views.returnFC, name = 'returnFC'),

	url(r'^MC/tags/$', views.chooseTagMC, name = 'MCtags'),
	url(r'^MC/(?P<category>[A-z]\w+ [A-z]\w+)/$', views.randomMC, name = 'randomMC'),
	url(r'^MC/(?P<category>[A-z]\w+)/$', views.randomMC, name = 'randomMC'),

	url(r'^MC/(?P<category>[A-z]\w+ [A-z]\w+)/(?P<q_id>\d+)/(?P<answer>[A-D]\b)/$', views.checkAns, name = 'checkAns'),
	url(r'^MC/(?P<category>[A-z]\w+)/(?P<q_id>\d+)/(?P<answer>[A-D]\b)/$', views.checkAns, name = 'checkAns'),
)

