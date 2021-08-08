from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    t1 = models.ManyToManyField('Scope', through='ArticleScope', related_name='t1')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    topic = models.CharField(max_length=256, verbose_name='Название', default='')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['topic']

    def __str__(self):
        return self.topic

class ArticleScope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='scopes')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='Тэг', related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name= 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['-is_main', 'scope']