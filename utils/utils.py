import random, uuid, io, base64
from django.utils.text import slugify

from PIL import Image, ImageFilter

def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        if instance.title:
            slug = slugify(instance.title)
        else:
            slug = slugify(uuid.uuid1())
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        # auto generate new slug
        rand_int = random.randint(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance


def get_filtered_image(image, action):
    img = Image.open(image)
    # print(img.format, img.size, img.mode)
    filtered_image=None
    if action == "NO_FILTER":
        filtered_image = img
    if action == "BLUR":
        filtered_image = img.filter(ImageFilter.BLUR)
    if action == "CONTOUR":
        filtered_image = img.filter(ImageFilter.CONTOUR)
    if action == "EDGE_ENHANCE":
        filtered_image = img.filter(ImageFilter.EDGE_ENHANCE)
    if action == "SHARPEN":
        filtered_image = img.filter(ImageFilter.SHARPEN)
    if action == "SMOOTH":
        filtered_image = img.filter(ImageFilter.SMOOTH)
    if action == "GRAY":
        filtered_image = img.convert("L")


        # ("CONTOUR", "Contour"),
        # ("EDGE_ENHANCE", "Edge Enhance"),
        # ("EDGE_ENHANCE_MORE", "Edge Enhance More"),
        # ("SHARPEN", "Sharpen"),
        # ("SMOOTH", "Smooth"),

    # Convert the filtered image to bytes
    filtered_image_bytes = io.BytesIO()
    filtered_image.save(filtered_image_bytes, format=img.format)
    filtered_image_bytes.seek(0)
    # Encode the image data as base64
    encoded_image = base64.b64encode(filtered_image_bytes.getvalue()).decode('utf-8')
    src = f"data:image/{img.format.lower()};base64,{encoded_image}"
    # # Generate HTML to display the image
    # html = f'<img src="{src}">'
    # # Display the HTML
    # print(html)
    return src 
