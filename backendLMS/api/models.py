from django.db import models

# Create Books models 
class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

# create users models
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

#create admin models
class Admins(models.Model):
    admin_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

# create book transaction models
class BookTransaction(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete= models.CASCADE)
    issue_status = models.CharField(max_length=50)
    is_retuned = models.BooleanField(default=False)
    issue_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(null=True)