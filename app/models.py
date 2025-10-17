from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class Report(models.Model):
    picture = models.ImageField(upload_to="media")
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)
    description=models.TextField()
    status = models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name