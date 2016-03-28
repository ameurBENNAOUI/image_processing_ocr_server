from werkzeug import secure_filename
from flask_wtf import Form
from flask_wtf.file import FileField
from flask import Flask,render_template,request,flash
from forms import ClientForm
from flask.ext.wtf import Form
from comm_client import send_file


app=Flask(__name__)
app.secret_key='wehajfhsdgf3876845FRtff%6@#4'
@app.route('/upload/',methods=('GET','POST'))
def upload():
    form=ClientForm()
    if request.method == 'GET':

        return render_template('index.html', form=form)
    if request.method=='POST':
        file = request.files['filename']
        if file :
          filename=secure_filename(form.filename.data.filename)

          print form.filename.data.filename
          file.save('uploads/'+filename)
          send_file(filename)
        return render_template('index.html', form=form)


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=12346,use_reloader=True)
