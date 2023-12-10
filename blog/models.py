from django.db import models

class User(models.Model):
 ID = models.AutoField(primary_key=True)
 username = models.CharField(max_length=100, unique=True)
 email = models.EmailField(unique=True)
 password = models.CharField(max_length=100)

class Post(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100)
    date_published = models.DateField()

class Comment(models.Model):
    ID = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comtent = models.TextField()
    date_posted = models.DateTimeField()

class Category(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

