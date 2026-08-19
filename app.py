from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_programminglanguage", methods=["GET","POST"])
def add_one_programminglanguage():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into programminglanguage (name) values (:name)",hey)
        user = query_db('select * from programminglanguage')

        return render_template("programminglanguageform.html", programminglanguages=user, one_user=one_user, the_title="add new programminglanguage")


    user = query_db('select * from programminglanguage')
    one_user = query_db("select * from programminglanguage limit 1", one=True)
    return render_template("programminglanguageform.html", programminglanguages=user, one_user=one_user, the_title="add new programminglanguage")

