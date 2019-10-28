from django.db import models




class Category(models.Model):
    name            = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title           = models.CharField(max_length=255)
    body            = models.TextField()
    created_on      = models.DateTimeField(auto_now_add=True)
    last_modified   = models.DateTimeField(auto_now=True)
    categories      = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.title



class Comment(models.Model):
    author          = models.CharField(max_length=100)
    body            = models.TextField()
    created_on      = models.DateTimeField(auto_now_add=True)
    post            = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.author






































