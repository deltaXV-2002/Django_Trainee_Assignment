from django.shortcuts import render
import threading
from .models import MyModel2
from django.http import HttpResponse
# Create your views here.
def test_signal(request):
    print(f"View is running in the same thread: {threading.current_thread().name}")
    MyModel2.objects.create(name = "Test Instance")
    print("object created")
    return HttpResponse("Check console for output")