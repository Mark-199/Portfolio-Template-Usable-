from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class SiteSettings(models.Model):
    name = models.CharField(max_length=100, default="Your Name")
    email = models.EmailField(default="your.email@example.com")
    github_url = models.URLField(default="https://github.com/yourusername")
    linkedin_url = models.URLField(default="https://linkedin.com/in/yourusername")

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name_plural = "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SiteSettings, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Me"