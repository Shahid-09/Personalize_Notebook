from flask_restful import Resource
from flask import Flask, request, session, jsonify
from app.md.model import User, Note
from app.md.serializer import UserSchema, NotesSchema
from app.auth.decorator import token_required
from app import db

class Noteview(Resource):
    @token_required
    def get(self):
        note = Note.query.filter_by(user_id=self.id)
        schema = NotesSchema().dump(note,many=True)
        return schema
    
    @token_required
    def post(self):
        schema = NotesSchema().load(request.get_json())
        new_note = Note(data = schema['data'],user_id = session['user_id'])
        db.session.add(new_note)
        db.session.commit()
        return NotesSchema().dump(new_note)
    
    @token_required
    def put(self):
        data = request.get_json()
        note = Note.query.filter_by(id = data['id'].update(data))
        db.session.commit()
        return jsonify({"message": "Data updated"})
    
    @token_required
    def delete(self):
        data = request.get_json()
        Note.query.filter_by(id = data['id']).delete()
        db.session.commit()
        return jsonify({"message": "Notes Deleted"})
    

