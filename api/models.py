from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Check if this field exists
    published_date = models.DateTimeField(null=True, blank=True)  # Ensure this field is here
