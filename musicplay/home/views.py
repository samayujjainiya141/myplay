from django.shortcuts import render
from . models import song
from django.http import JsonResponse
# Create your views here.
def index(request):
    data=song.objects.all()
    return render(request,'index.html',{'data':data})

def getdata(request): 
    id=request.GET['stid'] 
    print(id) 
    data = song.objects.filter(id=id) 
    return JsonResponse(list(data.values('song_name', 'artist','song')),safe=False)

