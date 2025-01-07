

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal Handler
@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print(f"Signal triggered for instance: {instance.name}")
    print("Simulating a long-running task...")
    time.sleep(5)  
    print("Signal processing completed.")
