from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyApp(models.Model):
    name = models.CharField(max_length=60, null=False)
    description = models.TextField(max_length=500, blank=True, default='')
    image = models.ImageField()
    src = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='apps', null=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = 'myapps'
        ordering = ['created_at']
