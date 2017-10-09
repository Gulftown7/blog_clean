from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 120)
    image = models.ImageField(null=True, blank=True, height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"post_id": self.id})
    
    def get_edit_url(self):
        return reverse("posts:post_update", kwargs={"post_id": self.id})
#         return "/posts/%s" %(self.id)

    def get_post_url(self):
        return reverse("posts:post_list")
    
    def post_delete(self):
        return reverse("posts:post_delete", kwargs={"post_id": self.id})
    
    class Meta:
        ordering = ["-timestamp", "-updated"]
    
    
    
    
    
    