from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyModel3(models.Model):
    name = models.CharField(max_length=100)

# Signal handler
@receiver(post_save, sender=MyModel3)
def create_child(sender, instance, **kwargs):
    print("Signal triggered")
    
    TestingModel.objects.create(name=f"tester of {instance.name}")
    print("Testingmodel object created")
        


class TestingModel(models.Model):
    name = models.CharField(max_length=100)
