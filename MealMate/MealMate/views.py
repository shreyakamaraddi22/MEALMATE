from django.http import HttpResponse


def hello(request):
    return HttpResponse("HEllo Django")

def thankyou(request):
    return HttpResponse("Thankyou Mr/Mrs Django!")