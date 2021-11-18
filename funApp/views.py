from django.shortcuts import render, redirect
from time import localtime, strftime
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request, 'index.html', context)

# ---------- Login / Registration ----------
def logReg(request):
    return render(request, 'forms/logReg.html')

# ---------- Dashboard ----------
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    note = Note.objects.all().values()
    context = {
        'user': user,
        'notes': Note.objects.all().values(),
    }
    print("user:", user)
    print("notes:", note)
    return render(request, 'dashboard.html', context)

# ---------- Add Note ----------
def addNote(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    return render(request, 'forms/addNote.html', context)

# ---------- View Single Note ----------
def viewNote(request):
    if 'user_id' not in request.session:
        return redirect('/')
    pass

# ---------- Update Note Landing ----------
def editNote(request):
    if 'user_id' not in request.session:
        return redirect('/')
    pass

# ---------- Add Task Landing ----------
def addTask(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    return render(request, 'forms/addTask.html', context)

# ---------- View Tasks ----------
def tasks(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'tasks': Task.objects.all().values(),
    }
    return render(request, 'tasks.html', context)

# ---------- View Single Task ----------
def viewTask(request):
    if 'user_id' not in request.session:
        return redirect('/')
    pass

# ---------- Update Task Landing ----------
def editTask(request):
    if 'user_id' not in request.session:
        return redirect('/')
    pass

# ---------- Add Upload Landing ----------
def addUpload(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    return render(request, 'forms/addUpload.html', context)

# ---------- View Uploads ----------
def uploads(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'uploads': Document.objects.all().values(),
    }
    return render(request, 'uploads.html', context)

# ---------- View Single Upload ----------
def viewUpload(request):
    if 'user_id' not in request.session:
        return redirect('/')
    pass


# -------------------- Form Routes -------------------------

# ---------- Login Route ----------
def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/')

# ---------- Register Route ----------
def register(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/logReg/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        email = request.POST['email'],
        username = request.POST['username'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/dashboard/')

# ---------- Create Note ----------
def createNote(request):
    Note.objects.create(
        noteTitle = request.POST['noteTitle'],
        noteText = request.POST['noteText'],
        user_id=request.POST['user'],
    )
    return redirect('/dashboard/')

# ---------- Create Task ----------
def createTask(request):
    Task.objects.create(
        task = request.POST['task'],
        desc = request.POST['desc'],
        user_id = request.POST['user'],
    )
    return redirect('/tasks/')

# ---------- Upload Route ----------
def createUpload(request):
    Document.objects.create(
        img = request.FILES['img'],
        imgName = request.POST['imgName']
    )
    return redirect('/uploads/')

# ---------- Update Note Route ----------
def updateNote(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.noteTitle = request.POST['noteTitle']
    toUpdate.noteText = request.POST['noteText']
    toUpdate.save()

    return redirect(f'/notes/{note_id}/')

# ---------- Update Task Route ----------
def updateTask(request, task_id):
    toUpdate = Task.objects.get(id=task_id)
    toUpdate.task = request.POST['task']
    toUpdate.desc = request.POST['desc']
    toUpdate.save()

    return redirect(f'/tasks/{task_id}/')


# -------------------- Logout / Delete Routes -------------------------

# ---------- Delete Note ----------
def deleteNote(request):
    pass

# ---------- Delete Task ----------
def deleteTask(request):
    pass

# ---------- Logout Route ----------
def logout(request):
    request.session.clear()
    return redirect('/')