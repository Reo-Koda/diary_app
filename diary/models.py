from django.db import models
from django.contrib.auth.models import User
from pathlib import Path
import uuid

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    title = models.CharField(max_length=120, verbose_name="タイトル")
    body = models.TextField(max_length=2000, verbose_name="本文")
    picture = models.ImageField(upload_to="diary/picture/", blank=True, null=True, verbose_name="画像")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="作成者")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kargs):
        picture = self.picture
        super().delete(*args, **kargs)
        if picture:
            Path(picture.path).unlink(missing_ok=True)