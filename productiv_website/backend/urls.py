from django.conf.urls import url

from backend import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'login/$', views.login_user, name="login"),
    url(r'controlpanel/$', views.controlpanel, name="controlpanel"),
    url(r'website/$', views.website, name="website")
]
