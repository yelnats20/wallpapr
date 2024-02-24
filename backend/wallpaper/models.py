from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class WallPaper(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField()
    tags = models.ManyToManyField('Tag', related_name='wallpaper_posts')
    created_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate slug from the title if not provided
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
