# Generated by Django 5.0.4 on 2024-04-15 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruds_api', '0002_book_file_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField(verbose_name='Telegram id')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cruds_api.book')),
            ],
        ),
    ]
