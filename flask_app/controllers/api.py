from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash, jsonify
import requests
from flask_app.models.user import User
from flask_cors import CORS

CORS(app)

@app.route('/api/looneytunes/')
def looneyTunes():
    if 'user_id' not in  session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.getOne(data)
        return render_template('looneyTunes.html', user=user)

@app.route('/api/squishies/')
def squishies():
    if 'user_id' not in  session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.getOne(data)
        return render_template('squishy.html', user=user)

# @app.route('/getTune/', methods=['POST'])
# def getTune():
#     request = requests.get(f'https://dojo.navyladyveteran.com/characters/')
#     print("print tunes: ", request.json())
#     return jsonify(request.json())
    

# @app.route('/getSquishy/', methods=['POST'])
# def getSquishy():
#     request = requests.get(f'https://dojo.navyladyveteran.com/squishies/')
#     print("print squishy: ", request.json())
#     return jsonify(request.json())


@app.route('/api/looneytunes/<int:id>/view/')
def showTune(id):
    data = id
    return render_template('viewTune.html', data=data)