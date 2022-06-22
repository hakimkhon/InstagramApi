from rest_framework import serializers
from .models import Story, User

class StorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('title', 'author', 'content', 'created')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
