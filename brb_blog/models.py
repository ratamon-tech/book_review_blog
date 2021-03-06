from django.db import models

# Create your models here.

class Topic(models.Model):
    """トピック"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """モデルの文字列を返す"""
        return self.text

class Entry(models.Model):
    """トピックの詳細"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """モデルの文字列を返す"""
        return f"{self.text[:25]}..."
