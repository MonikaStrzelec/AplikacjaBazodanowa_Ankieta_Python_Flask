import os
from flask import Flask, request, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SQLALCHEMY_DATABASE_URI'] =\
 'sqlite:///' + os.path.join(basedir, 'surveyData.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'keySecret' # powinien być zapisany w zmiennej środowiskowej nie w kodzie źródłowym #
migrate = Migrate(app, db)

class Survey(db.Model):
    __tablename__ = 'survey'
    id = db.Column(db.Integer, primary_key = True)
    question1 = db.Column(db.String, nullable = False)
    question2 = db.Column(db.Integer, nullable = False)
    question3 = db.Column(db.String, nullable = False)
    question4 = db.Column(db.String, nullable = False)
    question5 = db.Column(db.String, nullable = False)
    question6 = db.Column(db.String, nullable = False)
    question7 = db.Column(db.String, nullable = False)
    question8 = db.Column(db.String, nullable = False)
    question9 = db.Column(db.String, nullable = False)
    question10 = db.Column(db.String, nullable = False)
    question11 = db.Column(db.String, nullable = False)
    question12 = db.Column(db.String, nullable = False)

    def __init__(self, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12):
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3
        self.question4 = question4
        self.question5 = question5
        self.question6 = question6
        self.question7 = question7
        self.question8 = question8
        self.question9 = question9
        self.question10 = question10
        self.question11 = question11
        self.question12 = question12


class MainSiteForm(FlaskForm):
    submit = SubmitField('Przejdź do ankiety')


class Questionnaire(FlaskForm):
    question1 = IntegerField('1. Podaj swój wiek', validators=[InputRequired("Proszę podać wiek"), NumberRange(min=5, max=100)])
    question2 = RadioField('2. Podaj swoją płeć', [DataRequired("Jaka jest twoja płeć:")], choices=['mężczyzna', 'kobieta'])
    question3 = RadioField('3. Czy posiadasz rośliny w domu/ mieszkaniu?',
                            [InputRequired("Uzupełnij pytanie 3")],
                            choices=[('tak'), ('nie')])
    question4 = RadioField('4. Jak często podlewasz rośliny?',
                            [InputRequired("Uzupełnij pytanie 4")],
                            choices=[('raz w tygodniu'), ('co dwa tygodnie'), ('raz w miesiącu'), ('kiedy mi się przypomni'), ('tak czesto jak potrzebuja')])
    question5 = RadioField('5. Czy pamiętasz o podlewaniu roślin?',
                            [InputRequired("Uzupełnij pytanie 5")],
                            choices=[('tak'), ('nie'), ('czasami')])
    question6 = RadioField('6. Czy posiadasz ogrod?',
                            [InputRequired("Uzupełnij pytanie 6")],
                            choices=[('tak'), ('nie')])
    question7 = RadioField('7. Jesli posiadasz ogród to czy podlewasz rosliny w ogrodzie?',
                            [InputRequired("Uzupełnij pytanie 7")],
                            choices=[('tak'), ('nie'), ('czasami')])
    question8 = RadioField('8. Ile szacunkowo zajmuje ci casu podlanie roślin tygodniowo?',
                            [InputRequired("Uzupełnij pytanie 8")],
                            choices=[('mniej niż 5 min'), ('5 min'), ('15 min'), ('30 min'), ('45 min'), ('60 min'), ('> 60 min')])
    question9 = RadioField('9. Czy podlewając rozliny wiesz ile wody potrzebuje dana roślina i trzymasz się tych wytycznych?',
                            [InputRequired("Uzupełnij pytanie 9")],
                            choices=[('tak'), ('nie'), ('mniej więcej')])
    question10 = RadioField('10. Czy kożystasz z systemu nawadniania?',
                            [InputRequired("Uzupełnij pytanie 10")],
                            choices=[('tak'), ('nie')])
    question11 = RadioField('11. Czy kozystasz z aplikacji wspomagającej nawadnianie roślin?',
                            [InputRequired("Uzupełnij pytanie 11")],
                            choices=[('tak'), ('nie')])
    question12 = RadioField('12.  Czy kożystał byś z aplikacji wspomagajacej nawadnianie?',
                            [InputRequired("Uzupełnij pytanie 12")],
                            choices=[('tak'), ('raczej tak'), ('nie wiem'), ('raczej nie'), ('nie')])
    submit = SubmitField('Zapisz')


class QuestionnaireEdit(FlaskForm):
    id = IntegerField('Podaj numer id danych, które chcesz zmienić')
    question1 = IntegerField('Podaj swój wiek', validators=[InputRequired("Proszę podać wiek"), NumberRange(min=15)])
    question2 = RadioField('Podaj swoją płeć', [DataRequired("Musisz podać swoją płeć")], choices=['mężczyzna', 'kobieta'])
    question3 = RadioField('Czy posiadasz rośliny w domu/ mieszkaniu?',
                            [InputRequired("Uzupełnij pytanie 3")],
                            choices=[('tak'), ('nie')])
    question4 = RadioField('Jak często podlewasz rośliny?',
                            [InputRequired("Uzupełnij pytanie 4")],
                            choices=[('raz w tygodniu'), ('co dwa tygodnie'), ('raz w miesiącu'), ('kiedy mi się przypomni'), ('tak czesto jak potrzebuja')])
    question5 = RadioField('Czy pamiętasz o podlewaniu roślin?',
                            [InputRequired("Uzupełnij pytanie 5")],
                            choices=[('tak'), ('nie'), ('czasami')])
    question6 = RadioField('Czy posiadasz ogrod?',
                            [InputRequired("Uzupełnij pytanie 6")],
                            choices=[('tak'), ('nie')])
    question7 = RadioField('Jesli posiadasz ogród to czy podlewasz rosliny w ogrodzie?',
                            [InputRequired("Uzupełnij pytanie 7")],
                            choices=[('tak'), ('nie'), ('czasami')])
    question8 = RadioField('Ile szacunkowo zajmuje ci casu podlanie roślin tygodniowo?',
                            [InputRequired("Uzupełnij pytanie 8")],
                            choices=[('mniej niż 5 min'), ('5 min'), ('15 min'), ('30 min'), ('45 min'), ('60 min'), ('> 60 min')])
    question9 = RadioField('Czy podlewając rozliny wiesz ile wody potrzebuje dana roślina i trzymasz się tych wytycznych?',
                            [InputRequired("Uzupełnij pytanie 9")],
                            choices=[('tak'), ('nie'), ('mniej więcej'), (''), ('')])
    question10 = RadioField('Czy kożystasz z systemu nawadniania?',
                            [InputRequired("Uzupełnij pytanie 10")],
                            choices=[('tak'), ('nie')])
    question11 = RadioField('Czy kozystasz z aplikacji wspomagającej nawadnianie roślin?',
                            [InputRequired("Uzupełnij pytanie 11")],
                            choices=[('tak'), ('nie')])
    question12 = RadioField('Czy kożystał byś z aplikacji wspomagajacej nawadnianie?',
                            [InputRequired("Uzupełnij pytanie 12")],
                            choices=[('tak'), ('raczej tak'), ('nie wiem'), ('raczej nie'), ('nie')])
    submit = SubmitField('Zapisz edytowane dane')


@app.route('/')
def index():
    return render_template("index.html", current_time=datetime.utcnow())


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = Questionnaire()

    if form.validate_on_submit():
        question1 = request.form['question1']
        question2 = request.form['question2']
        question3 = request.form['question3']
        question4 = request.form['question4']
        question5 = request.form['question5']
        question6 = request.form['question6']
        question7 = request.form['question7']
        question8 = request.form['question8']
        question9 = request.form['question9']
        question10 = request.form['question10']
        question11 = request.form['question11']
        question12 = request.form['question12']

        record = Survey(question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12)
        db.session.add(record)
        db.session.commit()
        return redirect('/success')
    else:
        message = 'Wystąpił błąd'
        return render_template('survey.html', form=form, message=message)


@app.route('/edit', methods=['GET', 'POST'])
def edit():     
    form = QuestionnaireEdit()    

    if form.validate_on_submit():
        id = request.form['id']       
        person = Survey.query.filter_by(id=id).first()
        if person is None:              
            return render_template('errors.html', form=form)     
        question1 = request.form['question1']
        question2 = request.form['question2']
        question3 = request.form['question3']
        question4 = request.form['question4']
        question5 = request.form['question5']
        question6 = request.form['question6']
        question7 = request.form['question7']
        question8 = request.form['question8']
        question9 = request.form['question9']
        question10 = request.form['question10']
        question11 = request.form['question11']
        question12 = request.form['question12']
        db.session.commit()   
        return redirect('/successEdit') 
    else:
        message = 'Wystąpił błąd, nie możesz edytować danych'
        return render_template('edit.html', current_time=datetime.utcnow(), form=form, message=message)


@app.route('/success')
def success():
    return render_template('success.html', current_time=datetime.utcnow())


@app.route('/successEdit')
def successEdit():
    return render_template('successEdit.html', current_time=datetime.utcnow())


@app.route('/testResults')
def testResults():    
    numberWomen = 0
    number = Survey.query.count()
    listOfPeople = Survey.query.order_by(Survey.id)

    return render_template("testResults.html", current_time=datetime.utcnow(), listOfPeople=listOfPeople, number=number)


#EXCEPTIN HANDLING
@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def internal_server_error(e):
 return render_template("500.html", current_time=datetime.utcnow()), 500


#DEBUG MODE
if __name__ == "__main__":
    app.run(debug=True)