import os
from flask import Flask
from flask import flash, request, render_template 
from wtforms import Form, BooleanField, StringField,TextAreaField, RadioField, validators 



# create a wtform class which creates the inputs fields
class QuestionariesForm(Form):
    username     = StringField('Username ', [validators.Length(min=3, max=100)])
    gic          = StringField('GIC NO', [validators.InputRequired()])
    email        = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email("Write a correct email")])
    rateStudentAttendance = RadioField('Student Attendance', [], choices=[('verypoor', 'verypoor'), ('poor', 'poor'), ('good', 'good'),('verygood', 'verygood'),('execellent','execellent')])
    studentAttendance = TextAreaField('comment on student progress', [validators.Length(max=400)])
    studentGrade = RadioField('Grade', [], choices=[('E', 'verypoor'), ('D', 'poor'), ('C', 'good'),('B', 'verygood'),('A','execellent')])
    studentCommentsPerformance= TextAreaField('Comment on Student performance', [validators.Length(max=500)])
    accept= BooleanField('Accept and Submit', [validators.DataRequired()])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['FILE_NAME']  = 'answer.txt'
app.config['FILE_WRITE_MODE'] = 'w+'
app.config['FILE_APPEND_MODE'] = 'a+'


# open a file if the does not exist
if(not os.path.exists("/"+app.config['FILE_NAME'])):
    f = open(app.config['FILE_NAME'] , app.config['FILE_WRITE_MODE'])
    f.write("ANSWERS \n\n\n")
    f.close()

@app.route("/", methods=['GET', 'POST'])
def home():
    myform = QuestionariesForm(request.form)
    if request.method == 'POST' and myform.validate() and myform.accept.data == True:
        f = open(app.config['FILE_NAME'] , app.config['FILE_APPEND_MODE'])
        
            # append that information into text file
        f.write("\n\n Answers by "+myform.username.data +"\n\n")
        f.write("GIC No: "+myform.gic.data + "\n")
        f.write("Email: "+myform.email.data + "\n")
        f.write("Student Attandance Rating : \n"+myform.rateStudentAttendance.data+ "\n")
        f.write("Comment on Attendance Rating : "+myform.studentAttendance.data+ " \n\n")
        f.write("Grade given : "+myform.studentGrade.data+ "\n")
        f.write("Comments on Grade given : "+myform.studentCommentsPerformance.data+ "\n\n")
        f.close()
        flash("success", "Thanks for your feedback")
    # close the file when done
    
    return render_template('index.html',form=myform)




# start the server
if __name__ == '__main__':
 app.run(debug=True)