from flask import Flask, url_for
from flask.templating import render_template

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/employeedashboard')
def employeedashboard():
    return render_template('employeedashboard.html')

@app.route('/studentdashboard')
def studentdashboard():
    return render_template('studentdashboard.html')

@app.route('/addnewemployee')
def addnewemployee():
    return render_template('addnewemployee.html')

@app.route('/singlemployeeprofile')
def singlemployeeprofile():
    return render_template('singlemployee.html')

@app.route('/updateemployee')
def updateemployee():
    return render_template('updateemployee.html')

@app.route('/addnewstudent')
def addnewestudent():
    return render_template('addnewstudent.html')

@app.route('/singlstudentprofile')
def singlestudentprofile():
    return render_template('singlestudent.html')

@app.route('/updatestudent')
def updatestudent():
    return render_template('updatestudent.html')

@app.route('/studentperformance')
def studentperformance():
    return render_template('studentperformance.html')

def logout():
    render_template('home.html')

if __name__ =='__main__':
    app.run(debug = True)

