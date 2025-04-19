from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    tiltel = models.CharField(max_length=200)
    discription = models.TextField()
    complet = models.BooleanField(default=False)
    curntdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tiltel
    class Meta :
        ordering = ['complet']

# Create your models here.
