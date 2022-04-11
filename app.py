import os
from flask import Flask, request
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/run", methods=['POST'])
def run():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            #Run ML model to predict Oxygen Saturation in Arterial Blood
            
            return "SPO2: 98%"

if __name__ == "__main__":
    #load model
    app.run(host='0.0.0.0', port=8000, debug=True) # specify port=80