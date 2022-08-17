from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=128, verbose_name='Sarlavha')
    image = models.ImageField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(verbose_name='Maqola matni')

    #fields you need
    blog_view = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])

    # def get_region(self):
    #     return dict(Articles.regions)[self.region]

    # def get_category(self):
    #     return dict(Articles.categories)[self.category]
    