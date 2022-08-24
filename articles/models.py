from tabnanny import verbose
from django.db import models
from django.urls import reverse
from .const import Const 
from django.contrib.auth import get_user_model
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Articles(models.Model):
    regions = Const.regions
    categories = Const.categories

    title = models.CharField(max_length=128, verbose_name='Sarlavha')
    image = models.ImageField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    category = models.CharField(
        max_length=35,
        choices=categories,
        default=1
    )

    region = models.CharField(
        max_length=35,
        choices=regions,
        default=14
    )

    

    date = models.DateTimeField(auto_now_add=True)
    body = RichTextField(verbose_name="Maqola matni:")

    #fields you need
    blog_view = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])

    def get_region(self):
        return dict(Articles.regions)[self.region]

    def get_category(self):
        return dict(Articles.categories)[self.category]

    def get_date(self):
        now = self.date
        date_time = now.strftime("%d/%m/%Y")
        return date_time

   

    