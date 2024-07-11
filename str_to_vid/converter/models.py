from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    message = models.TextField(verbose_name='Сообщение')
    video = models.FileField(upload_to='videos/', verbose_name='Видео')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
