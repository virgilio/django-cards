# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'audience', views.AudienceViewSet, base_name='audience')
# router.register(r'authors', views.AuthorsViewSet, base_name='authors')
router.register(r'axis', views.AxisViewSet, base_name='axis')
router.register(r'cards', views.CardViewSet, base_name='cards')
router.register(r'tags', views.TagsViewSet, base_name='tags')
router.register(r'images', views.ImageViewSet, base_name='image')
router.register(r'youtube_embeds', views.YoutubeEmbedViewSet, base_name='youtube_embeds')
router.register(r'likes', views.LikeViewSet, base_name='likes')

urlpatterns = (
    url(r'^$', views.cards_view, name='cards_page'),
    url(r'^edit/$', views.card_edit_view, name='cards_edit_page'),
    url(r'^detail/$', views.card_detail_view, name='cards_detail'),
    url(r'^[0-9]$', views.card_detail_view, name='cards_detail_page'),
    url(r'^api/', include(router.urls)),
    url(r'^cards-list/$', views.cards_list_view, name='cards_list'),
    url(r'^new/$', views.card_new_view, name='cards_new'),
)
