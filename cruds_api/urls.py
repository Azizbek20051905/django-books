from django.urls import path
from .views import BookView, BookDetailView, MessageView, MessageDetailView, TopBookView, ChannelApiView, ChannelDetailView, MyLikeApiView, MyLikeDetailView, MyLikeUser
from .search import BookListView

urlpatterns = [
    path('book', BookView.as_view(), name="book"),
    path('top-book', TopBookView.as_view(), name="top-book"),
    path('booksearch', BookListView.as_view(), name="booksearch"),
    path('book/<int:pk>', BookDetailView.as_view(), name="book-detail"),
    path('message', MessageView.as_view(), name="message"),
    path('message/<int:pk>', MessageDetailView.as_view(), name="message_detail"),
    path('channel', ChannelApiView.as_view(), name="channel"),
    path('channel/<int:pk>', ChannelDetailView.as_view(), name="channel-detail"),
    path('my-like', MyLikeApiView.as_view(), name="like"),
    path('my-like/<int:pk>', MyLikeDetailView.as_view(), name="like-detail"),
    path('my-like/user/<int:userId>', MyLikeUser.as_view(), name="like-user"),
]