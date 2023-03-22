from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
data = []


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = 'static'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

#recieve pdf from client

@app.route('/pdf', methods=['POST'])
def pdf():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        data.append(f.filename)
        return redirect(url_for('display'))
        
@app.route('/pdf', methods=['GET'])
def get_pdf():
    return render_template('pdf.html')

@app.route("/display")
def display():
    print(data)
    return render_template('display.html', data=data)



app.run(debug=True, port=5000, host='127.0.0.1')