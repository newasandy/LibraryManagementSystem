# Generated by Django 5.1.2 on 2024-10-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
