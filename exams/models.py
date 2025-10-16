from django.db import models
from django.conf import settings

class sgexam(models.Model):
    title = models.CharField("Название экзамена", max_length=255)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)
    exam_date = models.DateField("Дата проведения экзамена")
    image = models.ImageField("Задание (изображение)", upload_to='exams/', blank=True, null=True)
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='sgexam_participants',
        verbose_name="Участники"
    )
    is_public = models.BooleanField("Опубликовано", default=False)

    def __str__(self):
        return f"{self.title} ({self.exam_date})"

    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"