from .models import Book, Message, Channel, MyLike
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

class MyLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLike
        fields = '__all__'