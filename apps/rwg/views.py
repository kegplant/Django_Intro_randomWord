from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):
    try:
        request.session['attemptNum']
    except:
        request.session['attemptNum']=0
    #return HttpResponse(response)
    return render(request,'rwg/index.html')
def random_word(request):
    try:
        request.session['attemptNum']
    except:
        request.session['attemptNum']=0
    request.session['attemptNum']+=1
    context={
        'random_word':get_random_string(length=14)
    }
    return render(request,'rwg/index.html',context)
def reset(request):
    try:
        request.session['attemptNum']
    except:
        request.session['attemptNum']=0
    request.session['attemptNum']=0
    return redirect('/')