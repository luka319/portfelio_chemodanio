from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


# В случае, когда вместо изображения
# требуется загрузить другой файл,
# нужно просто поменять ImageField на FileField.

# Местоположение загружаемых файлов image
# будет в MEDIA_ROOT/images. В Django локацией
# для MEDIA_ROOT по умолчанию является папка,
# откуда будут загружаться все файлы пользователя.

