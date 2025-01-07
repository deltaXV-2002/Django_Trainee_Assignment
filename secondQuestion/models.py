from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import threading
# Create your models here.
class MyModel2(models.Model):
    name = models.CharField(max_length=100)

# Signal Handler

@receiver(post_save , sender = MyModel2)
def my_handler(sender, instance, **kwargs):
    print(f"Signal triggered for : {instance.name}")
    print(f"handler is running in thread : {threading.current_thread().name}")