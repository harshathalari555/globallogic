from django.conf.urls import url

from . import views

app_name = "apps"
urlpatterns = [
    url(r'^$', views.home, name='recipe'),
    url(r'^create_category/$', views.create_category, name='create_category'),
    url(r'^save_category/$', views.save_category, name='save_category'),
    url(r'^(?P<recipe_id>[0-9]+)/details/$', views.details, name='details'),
    url(r'^(?P<recipe_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^add_image/(?P<id>\d+)', views.AddImage, name="addimage"),

]
