from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics,mixins
from .serializers import *
from .task import *
import time

class scraping_data(generics.GenericAPIView,mixins.CreateModelMixin):
    serializer_class = coin_detail
    queryset = currency_model.objects.all()

    # def get(self, request, *args, **kwargs):
    #     return self.list(request,*args,kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    

@api_view(['GET'])
def scraping_detail(request,pk):
    print(pk)
    currency = currency_model.objects.get(id = pk)
    currency_names = currency.names.split(',')
    print(currency_names)

    task = getting_the_data.delay(currency_names)
    result = task.get() 
    print('Result:', result)
    return Response(result)

