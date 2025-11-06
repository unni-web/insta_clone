from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file=models.FileField(upload_to='uploads/')
    
    def __str__(self):  
        return self.name

    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doc=models.FileField(upload_to='uploads/')
    
    def __str__(self):
        return str(self.doc)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
