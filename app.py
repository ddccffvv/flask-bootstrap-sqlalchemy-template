import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'doc', 'docx', 'xls', 'xlsx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 70 * 1024 * 1024
app.secret_key = os.urandom(24)

def allowed_file(name):
    """implement so only safe filenames are allowed"""
    return name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return render_template("success.html")
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
