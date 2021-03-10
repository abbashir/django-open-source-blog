from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class PostCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:category_wise_post', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, )
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, )
    feature = models.BooleanField(default=False)
    view_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('posts:post_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

