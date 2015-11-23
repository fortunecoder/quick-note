from django.conf.urls import url

from . import views

urlpatterns = [
	
	url(r'^$',views.index,name='index'),
	url(r'^notebook/(?P<nid>[a-zA-Z0-9]+)/$',views.notebook, name='notebook'),
	url(r'^note/(?P<qnoteid>[a-zA-Z0-9]+)/$',views.note, name='note'),
]