from django.conf.urls import url 
from revportal import views


urlpatterns = [
    url(r'^$', views.review_index, name='index'),
    url(r'^add_title/', views.add_newtitle, name='add_post'),
    url(r'^(?P<slug>[\w|\-]+)/$',views. one_title,name='post'),
    ]  