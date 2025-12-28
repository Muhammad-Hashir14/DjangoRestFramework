from django.db import models

# Create your models here.
class Blogs(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_content= models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.blog_title}-{self.blog_content[:20]}"

class Comments(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.comment[:20]}"