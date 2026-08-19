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


        one_user = query_db("insert into programminglanguage (name,short_name) values (:name,:short_name)",hey)
        user = query_db('select * from programminglanguage')

        return render_template("programminglanguageform.html", programminglanguages=user, one_user=one_user, the_title="add new programminglanguage")


    user = query_db('select * from programminglanguage')
    one_user = query_db("select * from programminglanguage limit 1", one=True)
    return render_template("programminglanguageform.html", programminglanguages=user, one_user=one_user, the_title="add new programminglanguage")

@app.route("/add_one_command_processing", methods=["GET","POST"])
def add_one_command_processing():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesprogramminglanguage= query_db("select * from programminglanguage")

        one_user = query_db("insert into command_processing (programminglanguage_id,type,description,script_or_cli) values (:programminglanguage_id,:type,:description,:script_or_cli)",hey)
        user = query_db('select * from command_processing')

        return render_template("command_processingform.html", command_processings=user, one_user=one_user, the_title="add new command_processing", touslesprogramminglanguage=touslesprogramminglanguage)


    touslesprogramminglanguage= query_db("select * from programminglanguage")

    user = query_db('select * from command_processing')
    one_user = query_db("select * from command_processing limit 1", one=True)
    return render_template("command_processingform.html", command_processings=user, one_user=one_user, the_title="add new command_processing", touslesprogramminglanguage=touslesprogramminglanguage)

@app.route("/add_one_switch", methods=["GET","POST"])
def add_one_switch():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesprogramming_language= query_db("select * from programming_language")

        one_user = query_db("insert into switch (name,programming_language_id,description,typeargument) values (:name,:programming_language_id,:description,:typeargument)",hey)
        user = query_db('select * from switch')

        return render_template("switchform.html", switchs=user, one_user=one_user, the_title="add new switch", touslesprogramming_language=touslesprogramming_language)


    touslesprogramming_language= query_db("select * from programming_language")

    user = query_db('select * from switch')
    one_user = query_db("select * from switch limit 1", one=True)
    return render_template("switchform.html", switchs=user, one_user=one_user, the_title="add new switch", touslesprogramming_language=touslesprogramming_language)

@app.route("/add_one_interprocess_communication", methods=["GET","POST"])
def add_one_interprocess_communication():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesprogramminglanguage= query_db("select * from programminglanguage")

        one_user = query_db("insert into interprocess_communication (programminglanguage_id,name,description,script) values (:programminglanguage_id,:name,:description,:script)",hey)
        user = query_db('select * from interprocess_communication')

        return render_template("interprocess_communicationform.html", interprocess_communications=user, one_user=one_user, the_title="add new interprocess_communication", touslesprogramminglanguage=touslesprogramminglanguage)


    touslesprogramminglanguage= query_db("select * from programminglanguage")

    user = query_db('select * from interprocess_communication')
    one_user = query_db("select * from interprocess_communication limit 1", one=True)
    return render_template("interprocess_communicationform.html", interprocess_communications=user, one_user=one_user, the_title="add new interprocess_communication", touslesprogramminglanguage=touslesprogramminglanguage)

@app.route("/add_one_way_handle_insecure_data", methods=["GET","POST"])
def add_one_way_handle_insecure_data():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesprogramminglanguage= query_db("select * from programminglanguage")

        one_user = query_db("insert into way_handle_insecure_data (programminglanguage_id,name,description,script) values (:programminglanguage_id,:name,:description,:script)",hey)
        user = query_db('select * from way_handle_insecure_data')

        return render_template("way_handle_insecure_dataform.html", way_handle_insecure_datas=user, one_user=one_user, the_title="add new way_handle_insecure_data", touslesprogramminglanguage=touslesprogramminglanguage)


    touslesprogramminglanguage= query_db("select * from programminglanguage")

    user = query_db('select * from way_handle_insecure_data')
    one_user = query_db("select * from way_handle_insecure_data limit 1", one=True)
    return render_template("way_handle_insecure_dataform.html", way_handle_insecure_datas=user, one_user=one_user, the_title="add new way_handle_insecure_data", touslesprogramminglanguage=touslesprogramminglanguage)

@app.route("/add_one_way_handle_insecure_code", methods=["GET","POST"])
def add_one_way_handle_insecure_code():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesprogramminglanguage= query_db("select * from programminglanguage")

        one_user = query_db("insert into way_handle_insecure_code (programminglanguage_id,name,description,script) values (:programminglanguage_id,:name,:description,:script)",hey)
        user = query_db('select * from way_handle_insecure_code')

        return render_template("way_handle_insecure_codeform.html", way_handle_insecure_codes=user, one_user=one_user, the_title="add new way_handle_insecure_code", touslesprogramminglanguage=touslesprogramminglanguage)


    touslesprogramminglanguage= query_db("select * from programminglanguage")

    user = query_db('select * from way_handle_insecure_code')
    one_user = query_db("select * from way_handle_insecure_code limit 1", one=True)
    return render_template("way_handle_insecure_codeform.html", way_handle_insecure_codes=user, one_user=one_user, the_title="add new way_handle_insecure_code", touslesprogramminglanguage=touslesprogramminglanguage)

@app.route("/add_one_generate_other_language_in_the_programming_language", methods=["GET","POST"])
def add_one_generate_other_language_in_the_programming_language():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesprogramminglanguage= query_db("select * from programminglanguage")

        touslesotherprogramminglanguage= query_db("select * from otherprogramminglanguage")

        one_user = query_db("insert into generate_other_language_in_the_programming_language (programminglanguage_id,otherprogramminglanguage_id,description,script) values (:programminglanguage_id,:otherprogramminglanguage_id,:description,:script)",hey)
        user = query_db('select * from generate_other_language_in_the_programming_language')

        return render_template("generate_other_language_in_the_programming_languageform.html", generate_other_language_in_the_programming_languages=user, one_user=one_user, the_title="add new generate_other_language_in_the_programming_language", touslesprogramminglanguage=touslesprogramminglanguage, touslesotherprogramminglanguage=touslesotherprogramminglanguage)


    touslesprogramminglanguage= query_db("select * from programminglanguage")

    touslesotherprogramminglanguage= query_db("select * from otherprogramminglanguage")

    user = query_db('select * from generate_other_language_in_the_programming_language')
    one_user = query_db("select * from generate_other_language_in_the_programming_language limit 1", one=True)
    return render_template("generate_other_language_in_the_programming_languageform.html", generate_other_language_in_the_programming_languages=user, one_user=one_user, the_title="add new generate_other_language_in_the_programming_language", touslesprogramminglanguage=touslesprogramminglanguage, touslesotherprogramminglanguage=touslesotherprogramminglanguage)

@app.route("/add_one_generate_the_programming_language_from_other_language", methods=["GET","POST"])
def add_one_generate_the_programming_language_from_other_language():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesprogramminglanguage= query_db("select * from programminglanguage")

        touslesfromotherprogramminglanguage= query_db("select * from fromotherprogramminglanguage")

        one_user = query_db("insert into generate_the_programming_language_from_other_language (programminglanguage_id,fromotherprogramminglanguage_id,description,script) values (:programminglanguage_id,:fromotherprogramminglanguage_id,:description,:script)",hey)
        user = query_db('select * from generate_the_programming_language_from_other_language')

        return render_template("generate_the_programming_language_from_other_languageform.html", generate_the_programming_language_from_other_languages=user, one_user=one_user, the_title="add new generate_the_programming_language_from_other_language", touslesprogramminglanguage=touslesprogramminglanguage, touslesfromotherprogramminglanguage=touslesfromotherprogramminglanguage)


    touslesprogramminglanguage= query_db("select * from programminglanguage")

    touslesfromotherprogramminglanguage= query_db("select * from fromotherprogramminglanguage")

    user = query_db('select * from generate_the_programming_language_from_other_language')
    one_user = query_db("select * from generate_the_programming_language_from_other_language limit 1", one=True)
    return render_template("generate_the_programming_language_from_other_languageform.html", generate_the_programming_language_from_other_languages=user, one_user=one_user, the_title="add new generate_the_programming_language_from_other_language", touslesprogramminglanguage=touslesprogramminglanguage, touslesfromotherprogramminglanguage=touslesfromotherprogramminglanguage)

@app.route("/add_one_translate_the_programming_language_to_other_language", methods=["GET","POST"])
def add_one_translate_the_programming_language_to_other_language():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesprogramminglanguage= query_db("select * from programminglanguage")

        touslesotherprogramminglanguage= query_db("select * from otherprogramminglanguage")

        one_user = query_db("insert into translate_the_programming_language_to_other_language (programminglanguage_id,otherprogramminglanguage_id,description,script) values (:programminglanguage_id,:otherprogramminglanguage_id,:description,:script)",hey)
        user = query_db('select * from translate_the_programming_language_to_other_language')

        return render_template("translate_the_programming_language_to_other_languageform.html", translate_the_programming_language_to_other_languages=user, one_user=one_user, the_title="add new translate_the_programming_language_to_other_language", touslesprogramminglanguage=touslesprogramminglanguage, touslesotherprogramminglanguage=touslesotherprogramminglanguage)


    touslesprogramminglanguage= query_db("select * from programminglanguage")

    touslesotherprogramminglanguage= query_db("select * from otherprogramminglanguage")

    user = query_db('select * from translate_the_programming_language_to_other_language')
    one_user = query_db("select * from translate_the_programming_language_to_other_language limit 1", one=True)
    return render_template("translate_the_programming_language_to_other_languageform.html", translate_the_programming_language_to_other_languages=user, one_user=one_user, the_title="add new translate_the_programming_language_to_other_language", touslesprogramminglanguage=touslesprogramminglanguage, touslesotherprogramminglanguage=touslesotherprogramminglanguage)

@app.route("/add_one_embedprogramminglanguageinascript", methods=["GET","POST"])
def add_one_embedprogramminglanguageinascript():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesprogramminglanguage= query_db("select * from programminglanguage")

        touslesscript_programminglanguage= query_db("select * from script_programminglanguage")

        one_user = query_db("insert into embedprogramminglanguageinascript (programminglanguage_id,script_programminglanguage_id,description,script) values (:programminglanguage_id,:script_programminglanguage_id,:description,:script)",hey)
        user = query_db('select * from embedprogramminglanguageinascript')

        return render_template("embedprogramminglanguageinascriptform.html", embedprogramminglanguageinascripts=user, one_user=one_user, the_title="add new embedprogramminglanguageinascript", touslesprogramminglanguage=touslesprogramminglanguage, touslesscript_programminglanguage=touslesscript_programminglanguage)


    touslesprogramminglanguage= query_db("select * from programminglanguage")

    touslesscript_programminglanguage= query_db("select * from script_programminglanguage")

    user = query_db('select * from embedprogramminglanguageinascript')
    one_user = query_db("select * from embedprogramminglanguageinascript limit 1", one=True)
    return render_template("embedprogramminglanguageinascriptform.html", embedprogramminglanguageinascripts=user, one_user=one_user, the_title="add new embedprogramminglanguageinascript", touslesprogramminglanguage=touslesprogramminglanguage, touslesscript_programminglanguage=touslesscript_programminglanguage)

