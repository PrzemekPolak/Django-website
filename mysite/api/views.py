from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import User_assetSerializer
from crypt.models import User_asset, Coin


# def coin_list(request):
    # if(request.method == 'GET'):
    #     data = Coin.get_cp()
    #     data = ser.serialize('json', Coin.get_cp(), fields=('coin_id','coin_name','price'))
    #     return JsonResponse(data,safe=False)

# class coin_list(viewsets.ModelViewSet):
#     queryset = Coin.objects.all()
#     serializer_class = Coin_listSerializer


def coin_list(request):
    if(request.method == 'GET'):
        data = list(Coin.objects.values())
        cp_data = Coin.get_cp()
        for x in range(len(data)):
            data[x]['current_price'] = cp_data[x]        
        return JsonResponse(data,safe=False)


@csrf_exempt
def user_asset(request):
    if(request.method == 'GET'):
        tasks = User_asset.objects.all()
        serializer = User_assetSerializer(tasks, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = User_assetSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# class user_asset(viewsets.ModelViewSet):
#     queryset = User_asset.objects.all()
#     serializer_class = User_assetSerializer


@csrf_exempt
def user_asset_detail(request, pk):
    try:
        # obtain the task with the passed id.
        task = User_asset.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = User_assetSerializer(task, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the task
        task.delete() 
        # return a no content response.
        return HttpResponse(status=204)