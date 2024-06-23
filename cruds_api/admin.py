from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Book, Message, Channel, MyLike

admin.site.unregister(Group)
admin.site.unregister(User)
