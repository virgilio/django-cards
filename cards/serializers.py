# -*- coding: utf-8 -*-
from __future__ import print_function
from rest_framework import serializers
from .models import Authors, Audience, Axis, Card, Like, YoutubeEmbed, Image
from django.contrib.auth import get_user_model
from drf_writable_nested import WritableNestedModelSerializer
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'biography', 'occupation', 'city')

class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = '__all__'

class AxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Axis
        fields = '__all__'

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('pk', 'author_name', 'author_description')

class ImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('pk', 'image', 'description')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('pk', 'user', 'card', 'created')

class YoutubeEmbedSerializer(serializers.ModelSerializer):

    url = serializers.CharField()

    class Meta:
        model = YoutubeEmbed
        fields =('pk', 'url')

class CardSerializer(TaggitSerializer, WritableNestedModelSerializer):

    audience = AudienceSerializer(required=False)
    author = AuthorSerializer(required=False)
    authors = AuthorsSerializer(many=True, required=False)
    axis = AxisSerializer(required=False)
    image_gallery = ImageGallerySerializer(many=True, required=False)
    likes = serializers.SerializerMethodField()
    tags = TagListSerializerField(required=False)
    youtube_embeds = YoutubeEmbedSerializer(many=True, required=False)

    def get_likes(self, obj):
        return obj.like_set.count()

    class Meta:
        model = Card
        fields = ('pk',
                  'audience',
                  'author',
                  'authors',
                  'axis',
                  'development',
                  'hint',
                  'image_gallery',
                  'is_certified',
                  'know_more',
                  'likes',
                  'tags',
                  'text',
                  'title',
                  'youtube_embeds',
                  'you_will_need')


class TagsInCardsSerializer(serializers.Serializer):
    name = serializers.CharField()
    slug = serializers.CharField()
