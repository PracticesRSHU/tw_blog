from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
#branch_Serhii
class CommentPost(models.Model):
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post=models.ForeignKey('Post', on_delete=models.CASCADE)
    text=models.TextField(max_length=300)
    created= models.DateTimeField(auto_now_add=True)
    moder=models.BooleanField(default=False)