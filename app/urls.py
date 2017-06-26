from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',        views.main,    name="main"),
    url(r'^convert/', views.convert, name="convert"),
    url(r'^submit/',  views.submit,  name="submit")
]