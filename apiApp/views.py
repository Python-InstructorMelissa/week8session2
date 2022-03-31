from django.shortcuts import render, redirect
from django.contrib import messages
from apiApp.models import *
import bcrypt

# ---------- Main landing page
def index(request):
    return render(request, 'index.html')

# ---------- Register / Login Functions
def register(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        username = request.POST['username'],
        email = request.POST['email'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/dashboard/')

def login(request):
    userName = User.objects.filter(username = request.POST['username'])
    userEmail = User.objects.filter(email = request.POST['email'])
    if userName:
        userLogin = userName[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/login/')
    if userEmail:
        userLogin = userEmail[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/login/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    messages.error(request, 'That email is not in our system')
    return redirect('/login/')


# ---------- Log Out
def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')


# ---------- Dashboard
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'images': Favorite.objects.all().values(),
        'uploads': Upload.objects.all().values(),
        'forecasts': Forecast.objects.all().values(),
    }
    print(Upload.objects.all().values())
    return render(request, 'dashboard.html', context)


# ---------- Favorites / Images Functions
def addImages(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'addImages.html', context)

def nasaImage(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'nasaImage.html', context)

def looneyToons(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'toons.html', context)

def createImage(request):
    Favorite.objects.create(
        name=request.POST['name'],
        img=request.POST['img'],
        user=User.objects.get(id=request.session['user_id']),
    )
    return redirect('/dashboard/')

def createUpload(request):
    Upload.objects.create(
        name=request.POST['name'],
        img=request.FILES['img'],
        user=User.objects.get(id=request.session['user_id']),
    )
    return redirect('/dashboard/')



# ---------- Weather Functions
def weather(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'weather.html', context)

def saveWeather(request):
    Forecast.objects.create(
        city=request.POST['city'],
        conditions=request.POST['conditions'],
        temp=request.POST['temp'],
        user=User.objects.get(id=request.session['user_id']),
    )
    return redirect('/dashboard/')




# ---------- User / Profile Functions
def users(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'you': user,
        'users': User.objects.all().values(),
    }
    return render(request, 'users.html', context)
