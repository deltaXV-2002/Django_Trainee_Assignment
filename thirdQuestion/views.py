
from django.db import transaction
from django.http import HttpResponse
from .models import MyModel3, TestingModel

def create_model(request):
    try:
        with transaction.atomic(): 
            print("Transaction started")
            
            mymodel = MyModel3.objects.create(name="mymodel Instance")
            print(f"Mymodel3 object count before exception: {MyModel3.objects.count()}")
            print(f"TestingModel object count before exception: {TestingModel.objects.count()}")
            
            raise Exception("Simulating an exception")
    except Exception as e:
        print(f"Exception occurred: {e}")

    
    mymodel_objectcount = MyModel3.objects.count()
    testingmodel_objectcount = TestingModel.objects.count()
    print(f"Mymodel3 count: {mymodel_objectcount}")
    print(f"Testing model count: {testingmodel_objectcount}")

    return HttpResponse("Check console for output")
