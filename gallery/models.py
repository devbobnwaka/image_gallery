from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from settings.base import AUTH_USER_MODEL
User = AUTH_USER_MODEL

from utils.utils import slugify_instance_title, get_filtered_image

# Create your models here.


class Image(models.Model):
    ACTION_CHOICES = (
        ("NO_FILTER", "No Filter"),
        ("BLUR", "Blur"),
        ("CONTOUR", "Contour"),
        ("EDGE_ENHANCE", "Edge Enhance"),
        ("EDGE_ENHANCE_MORE", "Edge Enhance More"),
        ("SHARPEN", "Sharpen"),
        ("SMOOTH", "Smooth"),
        ("GRAY", "Gray"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    description = models.TextField(null=True, blank=True)
    image_path = models.ImageField(upload_to="images")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={"slug": self.slug})

    def __str__(self):
        return f'{self.title}'


def image_pre_save(sender, instance, *args, **kwargs):
# print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)
        filtered_img = get_filtered_image(instance.image_path, instance.action)
        print(filtered_img)
        
pre_save.connect(image_pre_save, sender=Image)

def image_post_save(sender, instance, created, *args, **kwargs):
    # print('post_save')
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(image_post_save, sender=Image)

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
