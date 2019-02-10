from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

def gen_slug(string):
    new_slug = slugify(string, allow_unicode=True)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    category = models.ManyToManyField('Category', blank=True, related_name='posts')
    answer = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_pub']

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
