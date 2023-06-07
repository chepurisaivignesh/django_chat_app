from django.shortcuts import render,redirect
from .models import Message,Room
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,'login.html')

def room(request,room):
    username=request.GET.get('username')
    room_details=Room.objects.filter(roomcode=room)
    return render(request,'room.html',
    {
        'username':username,
        'roomcode':room,
        'room_details':room_details
    })
        
def checkroom(request):
    roomcode=request.POST['roomcode']
    username=request.POST['username']
    
    if Room.objects.filter(roomcode=roomcode).exists():
        return redirect("/"+roomcode+"/?username="+username)
    else:
        newroom=Room.objects.create(roomcode=roomcode)
        newroom.save()
        return redirect("/"+roomcode+"/?username="+username)

def send(request):
    message=request.POST['message']#this is the data we are getting from the form using ajax in javascript
    username=request.POST['username']
    roomcode=request.POST['roomcode']

    newmessage=Message.objects.create(roomcode=roomcode,messenger=username,content=message)

    newmessage.save()

    return HttpResponse('Message sent Successfully')

def getMessages(request,room):
    messages=Message.objects.filter(roomcode=room)
    return JsonResponse({"messages":list(messages.values())})
