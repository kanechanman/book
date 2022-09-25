from distutils.command.upload import upload
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Book(models.Model):
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)
    author = models.CharField("著者", max_length=255, blank=True)
    image = models.ImageField(upload_to = "media/", verbose_name="画像", null=True, blank=True)
    

def __str__(self):
    return self.name




class Impression(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='書籍', related_name='impressions')
    point = models.IntegerField("点数", validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    comment = models.TextField('コメント', blank=True)

def __str__(self):
    return self.comment








