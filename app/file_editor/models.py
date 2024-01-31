from django.db import models


class Files(models.Model):
    files = models.FileField('Файл', upload_to='files/')
    uploaded_at = models.DateTimeField('Дата и время загрузки', auto_now_add=True)
    processed = models.BooleanField('Обработка', default=False)

    def __str__(self):
        return f'Файл {self.id}'

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
