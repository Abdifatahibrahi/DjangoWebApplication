from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Towhid_Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}, {self.content}'
class Swalah_Posts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}, {self.content}'


class Article_Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}, {self.content}'

class Zakat_Posts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}, {self.content}'

class Swaum_Posts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}, {self.content}'

class Hajj_Posts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}, {self.content}'

class CouresalImage(models.Model):
    image = models.ImageField(blank=True, unique=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.title} {self.description}"



class Question(models.Model):
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.CharField(max_length=300)
    slug = models.SlugField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class Others(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    content = models.TextField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")


    def __str__(self):
        return f"{self.user.username} profile"


    def save(self, *args, **kwargs):
        super(Profile,self).save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.width > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
