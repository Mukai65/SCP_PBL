from scp.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from scp.database import db

class Student(db.Model):

    __tablename__ = 'student_table'

    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.String(255), db.ForeignKey('classcode_table.class_id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    day = db.Column(db.String(255), nullable=True)
    week = db.Column(db.Integer, nullable=True)
    month = db.Column(db.Integer, nullable=True)
    total = db.Column(db.Integer, nullable=True)
    group = db.Column(db.Integer, nullable=False)
    account = db.relationship('Account', backref='student_table', uselist=False)
    class_code = db.relationship('Class_Code', backref='student_table')
    

    def __init__(self, id, class_id, number, name, day=None, week=None, month=None, total=None, group=100):
        self.id = id
        self.class_id = class_id
        self.number = number
        self.name = name
        self.day = day
        self.week = week
        self.month = month
        self.total = total
        self.group = group


class Account(db.Model):

    __tablename__ = 'account_table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student_table.id'), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    student = db.relationship('Student', backref='account_table')


    def __init__(self, student_id, password):
        self.student_id = student_id
        self.password = password
        


class Class_Code(db.Model):

    __tablename__ = 'classcode_table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(db.String(255), unique=True, nullable=False)
    classname = db.Column(db.String(255), nullable=False)
    student = db.relationship('Student', backref='classcode_table')


    def __init__(self, class_id, classname):
        self.class_id = class_id
        self.classname = classname
