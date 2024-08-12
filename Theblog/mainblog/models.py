from django.db import models
from django.contrib.auth.models import User
from ckeditor .fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="category_name")
    category_image = models.ImageField(null=True, blank=True, upload_to="images/category_images/")

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="post_title")
    header_image = models.ImageField(null=True, blank=True, upload_to="images/posts/")
    title_tag = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    body = RichTextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category_posts')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='liked_pots', blank=True)

    class Meta:
        ordering = ['-post_date']
        verbose_name_plural = "Posts"

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title}"

    def total_comments(self):
        return self.comments.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = "Comments"

    def __str__(self):
        return f'{self.post}'
