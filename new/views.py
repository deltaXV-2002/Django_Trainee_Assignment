
from new.models import MyModel
from django.http import HttpResponse


def fun(request):

  MyModel.objects.create(name = "Test Instance2")
  MyModel.objects.create(name = "Test Instance4")
  
  print("Object created")
  return HttpResponse("check console for output")
# Create your views here.
