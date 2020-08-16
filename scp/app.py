from flask import Flask,render_template,request,redirect,session,url_for
from scp.database import init_db, db
from hashlib import sha256
from scp.models.models import Student,Account,Class_Code
from datetime import timedelta
import scp.models

def create_app():
  app = Flask(__name__)
  # DB設定を読み込む
  app.secret_key = 'SHERLOCKED'
  app.config.from_object('scp.config.Config')
  
  init_db(app)

  return app

app = create_app()

@app.route("/")
@app.route("/top")
def top():
    status = request.args.get("status")
    return render_template("Login_Web.html",status=status)


@app.route("/login",methods=["post"])
def login():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=1)
    user_id = request.form["ID"]
    id = Student.query.filter_by(id=user_id).first()
    if id:
      password = request.form["password"]
      #hasshed_password = sha256((user.id + password + key.SALT).encode("utf-8")).hexdigest
      #if id.hasshed_password == hasshed_password: #hash化する
      if id.account.password == password:          #hash化しない
        session["user_id"] = user_id
        return redirect(url_for("index"))
      else:
        return redirect(url_for("top",status="wrong_password"))
    else:
      return redirect(url_for("top",status="user_notfound"))


@app.route("/index")
def index():
    if "user_id" in session:
      name = session["user_id"]
      id = Student.query.filter_by(id=name).first()
      classname = id.class_code.classname
      class_id = id.class_id
      mon = Student.query.filter_by(class_id=class_id,day="mon",group=1).order_by(Student.number.asc()).all()
      tue = Student.query.filter_by(class_id=class_id,day="tue",group=1).order_by(Student.number.asc()).all()
      wed = Student.query.filter_by(class_id=class_id,day="wed",group=1).order_by(Student.number.asc()).all()
      thu = Student.query.filter_by(class_id=class_id,day="thu",group=1).order_by(Student.number.asc()).all()
      fri = Student.query.filter_by(class_id=class_id,day="fri",group=1).order_by(Student.number.asc()).all()
      return render_template("Clean_Manage.html",name=name, classname=classname, mons=mon, tues=tue, weds=wed, thus=thu, fris=fri)
    else:
      return redirect(url_for("top",status="logout"))

@app.route("/index_move", methods=["post"])
def index_move():
    if "user_id" in session:
      name = session["user_id"]
      id = Student.query.filter_by(id=name).first()
      classname = id.class_code.classname
      stu = Student.query.filter_by(id=18110005).first()
      stu.day = "thu"
      db.session.commit()
      return redirect(url_for("index"))
    else:
      return redirect(url_for("top",status="logout"))


@app.route("/logout")
def logout():
  session.pop("user_id",None)
  return redirect(url_for("top",status="logout"))

@app.route("/attendance")
def attendance():
    if "user_id" in session:
      name = session["user_id"]
      id = Student.query.filter_by(id=name).first()
      classname = id.class_code.classname
      class_id = id.class_id
      students = Student.query.filter_by(class_id=class_id,group=1).order_by(Student.number.asc()).all()
      return render_template("Attendance.html", name=name, classname=classname, students=students)
    else:
      return redirect(url_for("top",status="logout"))


@app.route("/account")
def account():
  if "user_id" in session:
      name = session["user_id"]
      id = Student.query.filter_by(id=name).first()
      classname = id.class_code.classname
      class_id = id.class_id
      students = Student.query.filter_by(class_id=class_id,group=1).order_by(Student.number.asc()).all()
      return render_template("account.html",name=name, classname=classname, students=students)
  else:
      return redirect(url_for("top",status="logout"))


@app.route("/a_edit")
def a_edit():
  if "user_id" in session:
      name = session["user_id"]
      students = Student.query.filter_by(id=18110002).first()
      return render_template("edit.html",students=students)
  else:
      return redirect(url_for("top",status="logout"))

@app.route("/edit_process", methods=["POST"])
def edit_process():
  if "user_id" in session:
      name = session["user_id"]
      print(request.form['name'])
      stu = Student.query.filter_by(id=18110002).first()
      stu.name = request.form.get('name')
      db.session.commit()
      return redirect(url_for("account"))
  else:
      return redirect(url_for("top",status="logout"))

@app.route("/a_create")
def a_create():
  if "user_id" in session:
      name = session["user_id"]
      return render_template("Create New.html")
  else:
      return redirect(url_for("top",status="logout"))

@app.route("/create_process", methods=["post"])
def create_process():
  if "user_id" in session:
      name = session["user_id"]

      id = Student.query.filter_by(id=name).first()
      class_id = id.class_id
      List = {}
      List['name'] = request.form['name']
      List['id'] = request.form['id']
      List['num'] = request.form['number']
      List['day'] = request.form['day']
      List['pass'] = request.form['password']
      stu = Student(List['id'],class_id,List['num'],List['name'],List['day'],0,0,0,1)
      acc = Account(List['id'],List['pass'])
      db.session.add(stu)
      db.session.add(acc)
      db.session.commit()
      return redirect(url_for("account"))
  else:
      return redirect(url_for("top",status="logout"))

@app.route("/delete",methods=["POST"])
def delete():
  if "user_id" in session:
        name = session["user_id"]
        stu = Student.query.filter_by(id=18110001).first()
        acc = Account.query.filter_by(student_id=18110001).first()
        db.session.delete(acc)
        db.session.delete(stu)
        db.session.commit()
        return redirect(url_for("account"))
  else:
      return redirect(url_for("top",status="logout"))