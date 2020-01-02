from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404



def index(request):

    return render(request, 'index.html')


def iframe1(request):

    return render(request, '_frame1.html')

def iframe2(request):

    return render(request, '_frame2.html')

