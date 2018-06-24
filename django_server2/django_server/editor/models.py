from django.db import models

class Document(models.Model):
    editor = models.TextField()
    title = models.CharField(max_length=200)
    html = models.TextField()
    css = models.TextField()