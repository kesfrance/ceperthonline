"""ceperth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .settings import MEDIA_ROOT
from revportal import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ceperth import settings

urlpatterns = [
    url(r'^$', views.user_login, name='login'),
    url(r'^login/$', views.user_login, name='login'),#('revportal.urls')),
    url(r'^reviewportal/', include('revportal.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
    url(r'^signup/$', views.user_signup, name='signup'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),

] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

urlpatterns += staticfiles_urlpatterns()