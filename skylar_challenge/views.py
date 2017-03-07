from django.shortcuts import render
from django.http import JsonResponse

from skylar_challenge.chat import publish_subscribe


def index(request):
    return render(request, 'skylar_challenge/index.html', {})


def format_message(message, author='Dio'):
    if message is None:
        return None
    return {
        'sender': author,
        'message': message.decode('UTF-8')
    }


# TODO: redis subscribe
def subscribe(request):
    pub_sub = publish_subscribe.ChatRedis()
    message = pub_sub.receive()
    formated_message = format_message(message)
    return JsonResponse(formated_message, safe=False)


# TODO: redis publish
def publish(request):
    pub_sub = publish_subscribe.ChatRedis()
    sended_to = pub_sub.send('something'.encode('UTF-8'))
    if sended_to > 1:
        # What do?
        print("Sended to: ", sended_to)
    return JsonResponse({'listening': sended_to})
    # return render(request, 'skylar_challenge/index.html', {})
