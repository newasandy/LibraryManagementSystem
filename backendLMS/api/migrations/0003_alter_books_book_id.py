# Generated by Django 5.1.2 on 2024-10-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_books_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_id',
            field=models.IntegerField(default=1),
        ),
    ]
