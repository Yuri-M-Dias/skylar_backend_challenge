from django.shortcuts import render
from django.http import JsonResponse

from skylar_challenge.chat import publish_subscribe


def index(request):
    return render(request, 'skylar_challenge/index.html', {})


# TODO: redis subscribe
def subscribe(request):
    pub_sub = publish_subscribe.ChatRedis()
    message = pub_sub.receive()
    if message is not None:
        # TODO: parse message
        return JsonResponse({
            'sender': 'Dio',
            'message': message
        })
    return JsonResponse(None)
    #return render(request, 'skylar_challenge/index.html', {})


# TODO: redis publish
def publish(request):
    pub_sub = publish_subscribe.ChatRedis()
    sended_to = pub_sub.send('something')
    if sended_to > 1:
        # What do?
        print("Sended to: ", sended_to)
    return JsonResponse({'listening': sended_to})
    #return render(request, 'skylar_challenge/index.html', {})
