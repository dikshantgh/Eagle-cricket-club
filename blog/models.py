from cloudinary.models import CloudinaryField
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
import uuid


class Blog(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(auto_now=True, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    content = models.TextField(db_index=True)
    display_picture = CloudinaryField(db_index=True)
    total_view = models.IntegerField(db_index=True, default=0)
    slug = models.SlugField(db_index=True, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)
    image_source = models.CharField(max_length=1000, db_index=True, blank=True, null=True)
    tag = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug, 'uuid': self.uuid})

    def set_view(self):
        self.total_view += 1
        self.save()

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(**kwargs)

    class Meta:
        ordering = ['-total_view']


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment', db_index=True)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    comment_text = models.TextField(db_index=True)
    commented_date = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.commented_by.username} commented on {self.blog}"

    class Meta:
        ordering = ['commented_date']
