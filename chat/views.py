from django.shortcuts import render,redirect

def index(request):
    if 'room_name' in request.GET:
        room_name = request.GET['room_name']
        return redirect('room', room_name=room_name)
    return render(request, 'index.html')


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
