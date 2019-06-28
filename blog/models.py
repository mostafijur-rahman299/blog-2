from django.db import models
from django.urls  import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

from tinymce.models import HTMLField


class Post(models.Model):
    author          = models.ForeignKey(User, on_delete=models.CASCADE)
    title           = models.CharField(max_length=200)
    description     = HTMLField()
    is_draft        = models.BooleanField(default=True)
    create_date     = models.DateTimeField(auto_now_add=True)
    update_date     = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-create_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={"pk": self.pk})





