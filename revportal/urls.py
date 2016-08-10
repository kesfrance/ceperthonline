from django.conf.urls import url 
from revportal import views


urlpatterns = [
    url(r'^$', views.all_titles, name='index'),
    url(r'^add_newtitle/', views.add_newtitle, name='add_newtitle'),
    url(r'^(?P<slug>[\w|\-]+)/$',views.one_title, name='all_titles'),
    ]  