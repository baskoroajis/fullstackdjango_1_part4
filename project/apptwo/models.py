from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=250, unique=True)
    last_name = models.CharField(max_length=250, unique=False)
    email = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.first_name


class Article(models.Model):
    article_name = models.CharField(max_length=250, unique=True)
    def __str__(self):
        return self.article_name


