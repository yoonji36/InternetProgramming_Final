from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='mall/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #자동 날짜 생성
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/mall/{self.pk}'

    #author

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # on_delete->포스트를 지우면 댓글도 지움
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)