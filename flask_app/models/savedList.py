from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import note, listNote

class SavedList:
    db='notes'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.user_id = data['user_id']
        self.createdAt = data['createdAt']
        self.updateAT = data['updatedAT']
        self.listNotes = []

    @classmethod
    def getAll(cls):
        q = 'SELECT * FROM savedList;'
        r = connectToMySQL(cls.db).query_db(q)
        lists = []
        for list in r:
            lists.append(cls(list))
        return lists

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM savedList WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getUserLists(cls, data):
        query = "SELECT * FROM savedList WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print('userlists model results: ', results)
        lists = []
        for list in results:
            lists.append(cls(list))
        return lists

    @classmethod
    def save(cls, data):
        q = 'INSERT INTO savedList (name, user_id) VALUES (%(name)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(q, data)

    @classmethod
    def update(cls, data):
        q = 'UPDATE savedList SET name=%(name)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(q, data)

    @classmethod
    def delete(cls, data):
        q = 'DELETE FROM savedList WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(q, data)

    @classmethod
    def getListWithNotes(cls, data):
        q = 'SELECT FROM savedList LEFT JOIN savedList_has_note ON savedList_id = savedList.id LEFT JOIN note on note.id = note_id WHERE savedList.id = %(id);'
        r = connectToMySQL(cls.db).query_db(q, data)
        print("list with notes: ", r)
        return r