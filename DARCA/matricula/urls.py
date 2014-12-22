__author__ = 'Gustavo'

from django.conf.urls import patterns, url

from matricula import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^consultas/$', views.consultas, name='consultas'),
    url(r'^disciplinas/(?P<id>\d+)/$', views.disciplinas, name='disciplinas'),
    url(r'^matricular/(?P<id_aluno>\d+)/(?P<id_disciplina>\d+)/$', views.matricular, name='matricular'),
    url(r'^comprovante/(?P<id>\d+)$', views.comprovante, name='comprovante'),
    url(r'^mostraralunos/(?P<id>\d+)/$', views.mostraralunos, name='mostraralunos'),


)
