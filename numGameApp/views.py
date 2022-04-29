from django.shortcuts import render, redirect
from django.contrib import messages
from imagesApp.models import *
import random

def numIndex(request):
    # if request.method == 'GET':
    #     return redirect('numDash/')
    # # print(context)
    # else:
    context = {
        'results': request.session['results']
    }
    print("context", context)
    return render(request, 'numIndex.html', context)

# def numIndex(request):
#     if request.method == 'GET':
#         return redirect('numDash/')
#     return render(request, 'numIndex.html')

def addName(request):
    request.session['results'] = {
        'player': request.POST['player']
    }
    print("addName", request.session['results'])
    return redirect('/numGame/')

def numDash(request):
    return render(request, 'numDash.html')


# hidden method (form) to take play name and put into session
# take players guess put into session
# clear session - all and all just number