from django.db import models

# Create your models here.
class Book(models.Model):
    TYPES = [
        ("audio","audio"),
        ("document","document"),
    ]
    name = models.CharField(verbose_name="Kitob nomi", max_length=255)
    file_id = models.CharField(verbose_name="file_id", max_length=255)
    file_type = models.CharField(verbose_name='file_type', max_length=255, choices=TYPES)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    text = models.TextField()

class Channel(models.Model):
    name = models.CharField(verbose_name="Channel", max_length=255)
    link = models.TextField(verbose_name="Link", max_length=255)

class MyLike(models.Model):
    telegram_id = models.IntegerField(verbose_name="Telegram id")
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    