from django.db import models

class Photo(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
