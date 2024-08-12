from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home")
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # con la siguiente línea al terminar, obtendremos el URL con la nueva entrada
        # return reverse("article_details", args=(str(self.id)))
        # en este caso, devolveremos el home
        return reverse("home")
    
    def get_formatted_created(self):
        """Formats the 'created' field in various ways."""
        return self.created.strftime("%a, %b %d, %Y")  # Example format

    def get_formatted_modified(self):
        """Formats the 'modified' field in various ways."""
        return self.modified.strftime("%Y-%m-%d at %H:%M:%S")  # Example format
