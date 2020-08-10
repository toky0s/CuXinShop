from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('Public date')
    description = models.TextField()

    def __str__(self):
        return self.tag_name


class Article(models.Model):

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Public date')
    content = models.TextField()

    def __str__(self):
        return self.title
