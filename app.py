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
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                #Run ML model to predict Oxygen Saturation in Arterial Blood
                return "SPO2: 98%"
            else:
                return ""
        else:
            return ""
    else:
        return ""
            

if __name__ == "__main__":
    #load model
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
