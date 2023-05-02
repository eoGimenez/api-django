from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'


class Comment(models.Model):
    title = models.CharField(max_length=200)
    comment = models.TextField()
    created_by = models.CharField(default='test', max_length=50)
    in_post = models.ForeignKey(Post, null=True,  on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
