from re import L
from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.note import Note
from flask_app.models.user import User
from flask_app.models.savedList import SavedList
from flask_app.models.listNote import ListNote

@app.route('/user/<int:user_id>/list/')
def usersLists(user_id):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        user_id = {
            'user_id': user_id
        }
        user = User.getOne(data)
        lists = SavedList.getUserLists(user_id)
        return render_template('usersLists.html', user=user, lists=lists)

@app.route('/list/create/', methods=['POST'])
def createList():
    data = {
        'name': request.form['name'],
        'user_id': request.form['user_id'],
    }
    SavedList.save(data)
    flash('List Created')
    data1 = {
        'id': session['user_id']
    }
    user = User.getOne(data1)
    print('printing data save from list controller: ', data)
    return redirect(f'/user/{user.id}/list/')

@app.route('/list/<int:savedList_id>/view')
def viewList(savedList_id):
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        data1 = {
            'id': savedList_id
        }
        user = User.getOne(data)
        list = SavedList.getOne(data1)
        notes = Note.getAll()
        listNotes = ListNote.listNotes(data1)
        altListNotes = SavedList.getListWithNotes(data1)
        print("listNotes:", listNotes)
        return render_template('viewList.html', user=user, list=list, notes=notes, listNotes=altListNotes)

@app.route('/list/addNote/', methods=['POST'])
def listAddNote():
    data = {
        'savedList_id': request.form['savedList_id'],
        'note_id': request.form['note_id']
    }
    ListNote.save(data)
    flash('Note added to list')
    print("printing data", data)
    return redirect('/dashboard/')