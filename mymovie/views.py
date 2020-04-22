from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Bookserializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Au(View):
    book = Book.objects.all()
    #book = Book.objects.filter(is_open=True)
   # book = Book.objects.get(id=7)
    #output = ''
   # for b in book:
    #   output += f"i have {book.title()} kdkald<br>"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('jlkjlkjlk')


def sec(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'data': books})


class Bookviewset(viewsets.ModelViewSet):
    serializer_class = Bookserializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
