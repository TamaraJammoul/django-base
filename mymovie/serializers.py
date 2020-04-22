from rest_framework import serializers
from .models import Book, BookNum, Characters, Author


class BookNumserializer(serializers.ModelSerializer):
    class Meta:
        model = BookNum
        fields = ['id', 'isbn_10', 'isbn_13']


class Charactersserializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = ['id', 'name']


class Authorserializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname']


class Bookserializer(serializers.ModelSerializer):
    number = BookNumserializer(many=False)
    character = Charactersserializer(many=True)
    author = Authorserializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'description',
                  'cover', 'is_open', 'number', 'character', 'author']


class Bookminiserializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title']
