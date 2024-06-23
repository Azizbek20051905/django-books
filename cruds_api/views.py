from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Book, Message, Channel, MyLike
from django.shortcuts import redirect, render ,get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import BookSerializer, MessageSerializer, ChannelSerializer, MyLikeSerializer

# Create your views here.
class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True)
        return Response({"book": serializer_data.data})
    
    @csrf_exempt
    def post(self, request):
        serializer_data = BookSerializer( data=request.data )
        if serializer_data.is_valid():
            book = serializer_data.save()
            return Response({"status":"ok", "book": serializer_data.data})
        return Response({"status":"error", "book": serializer_data.errors })

class TopBookView(APIView):
    def get(self, request):
        books = Book.objects.all().order_by('-likes')[:10]
        serializer_data = BookSerializer(books, many=True)
        return Response({"book": serializer_data.data})

# Detail views page
class BookDetailView(APIView):
    def get(self, request,pk):
        book = Book.objects.filter(id=pk)
        if book:
            serializer_data = BookSerializer(book[0])
            return Response( {"book":serializer_data.data} )
        return Response( {"book":{"status":"error"}} )
    
    def put(self, request,pk):
        book = Book.objects.filter(id=pk)
        if book:
            book = book[0]
            number = int(request.data.get('likes')) + book.likes
            likes = number
            book.likes = likes

            book.save()
            serializer_data = BookSerializer(book)
            return Response( {"status":"success", "book":serializer_data.data} )
        return Response( {"status":"error", " detail":"Object not found "} )

class MessageView(APIView):
    def get(self, request):
        message = Message.objects.filter()
        serializer_data = MessageSerializer(message, many=True)
        return Response({"message": serializer_data.data})

class MessageDetailView(APIView):
    def get(self, request,pk):
        message = Message.objects.filter(id=pk)
        if message:
            serializer_data = MessageSerializer(message[0])
            return Response( {'status':'success', "message":serializer_data.data} )
        return Response( {"status":"error"} )
    
    def put(self, request,pk):
        message = Message.objects.filter(id=pk)
        if message:
            message = message[0]
            print()
            print(message.text)
            print()
            text = request.data.get('text')
            message.text = text
            message.save()
            serializer_data = MessageSerializer(message)
            return Response( {"status":"success", "message":serializer_data.data} )
        return Response( {"status":"error", " detail":"Object not found "} )

class ChannelApiView(APIView):
    def get(self, request):
        books = Channel.objects.all()
        serializer_data = ChannelSerializer(books, many=True)
        return Response({"channel": serializer_data.data})
    
    @csrf_exempt
    def post(self, request):
        serializer_data = ChannelSerializer( data=request.data )
        if serializer_data.is_valid():
            channel = serializer_data.save()
            return Response({"status":"ok", "channel": serializer_data.data})
        return Response({"status":"error", "channel": serializer_data.errors})

class ChannelDetailView(APIView):
    def get(self, request,pk):
        channel = Channel.objects.filter(id=pk)
        if channel:
            serializer_data = ChannelSerializer(channel[0])
            return Response( {"channel":serializer_data.data} )
        return Response( {"channel":{"status":"error"}} )
    
    def put(self, request,pk):
        channel = Channel.objects.filter(id=pk)
        if channel:
            channel = channel[0]
            name = request.data.get('name')
            link = request.data.get('link')
            
            channel.name = name
            channel.link = link

            channel.save()
            serializer_data = ChannelSerializer(channel)
            return Response( {"status":"success", "channel":serializer_data.data} )
        return Response( {"status":"error", " detail":"Object not found "} )
    
    def delete(self, request, pk):
        channel = Channel.objects.filter(id=pk)
        channel.delete()
        return Response({"status":"success"})

class MyLikeApiView(APIView):
    def get(self, request):
        like_book = MyLike.objects.all()
        serializer_data = MyLikeSerializer(like_book, many=True)
        return Response({"like_book": serializer_data.data})
    
    @csrf_exempt
    def post(self, request):
        serializer_data = MyLikeSerializer( data=request.data )
        if serializer_data.is_valid():
            like_book = serializer_data.save()
            return Response({"status":"ok", "like_book": serializer_data.data})
        return Response({"status":"error", "like_book": serializer_data.errors})

class MyLikeDetailView(APIView):
    def get(self, request,pk):
        like_book = MyLike.objects.filter(id=pk)
        if like_book:
            serializer_data = MyLikeSerializer(like_book[0])
            return Response( {"like_book":serializer_data.data} )
        return Response( {"like_book":{"status":"error"}} )
    
    def put(self, request,pk):
        like_book = MyLike.objects.filter(id=pk)
        if like_book:
            like_book = like_book[0]
            telegram_id = request.data.get('telegram_id')
            books = request.data.get('books')
            
            like_book.telegram_id = telegram_id
            like_book.books = books

            like_book.save()
            serializer_data = MyLikeSerializer(like_book)
            return Response( {"status":"success", "like_book":serializer_data.data} )
        return Response( {"status":"error", " detail":"Object not found "} )

    def delete(self, request, pk):
        like_book = MyLike.objects.filter(id=pk)
        like_book.delete()
        return Response({"status":"success"})

class MyLikeUser(APIView):
    def get(self, request, userId):
        like_books = MyLike.objects.filter(telegram_id=userId)
        if like_books:
            serializer_data = MyLikeSerializer(like_books, many=True)
            return Response({"status":"success", "like_book": serializer_data.data})
        return Response({"status":"error"})