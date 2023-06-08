from django.db import models
from settings.base import AUTH_USER_MODEL
User = AUTH_USER_MODEL

# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image_path = models.ImageField(upload_to="images")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class ImageTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Share(models.Model):
    READ_ONLY = 'RO'
    READ_WRITE = 'RW'
    CATEGORY_CHOICES = [
        (READ_ONLY,"read-only"),
        (READ_WRITE,"read-write"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    permission = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=READ_ONLY)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
