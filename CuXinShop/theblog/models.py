from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from unidecode import unidecode
from datetime import datetime


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_full_name = models.CharField(max_length=100, default='Fullname is none')
    pub_date = models.DateTimeField('Public date')
    description = models.TextField()

    def __str__(self):
        return self.tag_name

    def get_raw_name(self):
        return unidecode(self.tag_full_name)


class Article(models.Model):

    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Public date', auto_now_add=True)
    content = RichTextUploadingField(blank=False)
    view = models.IntegerField(default=0)
    last_modify = models.DateTimeField(null=True, auto_now_add=True)
    slug = models.SlugField(max_length=200, default='this-is-slug')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        self.last_modify = datetime.now()
        super().save(*args, **kwargs)