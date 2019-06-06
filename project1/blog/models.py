from django.db import models
from django.utils import timezone


class Category(models.Model):
    #Define category type
    name = models.CharField('カテゴリ名', max_length = 50)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__ (self):
        return self.name






class Post(models.Model):
    #Define post data contents

    title = models.CharField('タイトル', max_length = 50)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__ (self):
        return self.title
