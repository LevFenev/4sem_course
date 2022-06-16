from importlib import import_module
from unicodedata import name
from rest_framework.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    filter_backends=[filters.SearchFilter, DjangoFilterBackend]
    filterset_fields=['type']
    search_fields=['heading', 'description']
    
    @action(methods=['GET'], detail=False)
    def news(self, request):
        news = Post.objects.filter(Q(type__name='Новости большого спорта') | Q(type__name='Новости локального спорта'))
        data=PostSerializer(news,many=True).data
        return Response(data)
    
    @action(methods=['POST'], detail=True)
    def changetype(self, request, pk = None):
        if 'type_id' not in request.data:
            raise ValidationError({'type_id':'Необходим ID типа'})
        type_id=request.data['type_id']
        try:
            post=Post.objects.get(id=pk)
        except Post.DoesNotExist:
            raise ValidationError({'post':'Указанного поста не существует'})
        try:
            type=Type.objects.get(id=type_id)
        except Type.DoesNotExist:
            raise ValidationError({'type':'Указанного типа не существует'})
        post.type=type
        post.save()
        data=PostSerializer(post).data
        return Response(data)

class TypeViewSet(ModelViewSet):
    queryset=Type.objects.all()
    serializer_class=TypeSerializer