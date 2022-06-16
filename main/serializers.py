from rest_framework import serializers
from .models import *
from langdetect import detect

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
          
    def validate_heading(self, value):
        if ((detect(value) != 'ru') and (detect(value) != 'bg')):
            print(value, detect(value))
            raise serializers.ValidationError('Пишите на русском.')
        return value


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
