from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField('name', max_length=200)
    text01 = models.TextField('Text', blank=True)
    is_published = models.BooleanField(name = 'is_published', default=False)
    # is_pub123 = models.NullBooleanField(name = 'Опубликовано ли')
    timestamp = models.DateTimeField(null=True)
         

    def __str__(self):
         return '%s' % (self.name)
         return self.text01


