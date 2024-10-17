from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)