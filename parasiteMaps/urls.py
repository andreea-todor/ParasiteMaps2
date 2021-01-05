from django.conf.urls import url
from django.urls import re_path

from . import views

urlpatterns = [
    url(r'^$', views.default_map,name='default-page'),
    re_path(r'For more parasites/',views.more_parasites,name='more-parasites-page'),
    re_path(r'Plasmodiun/',views.plasmodium_map,name='plasmodium-page'),
    re_path(r'Leishmania/',views.leishmania_map,name='leishmania-page'),
    re_path(r'Trypanosoma/',views.trypanosoma_map,name='trypanosoma-page'),
    re_path(r'Ascaris Lumbricoides/',views.ascaris_lumbricoides_map,name='ascaris-lumbricoides-page'),
    re_path(r'Trichinella Spiralis/',views.trichinella_spiralis_map,name='trichinella-spiralis-page'),
]