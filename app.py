import os,shutil, pathlib
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from vision import crop_image

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'

app = Flask(__name__, static_url_path="/static")
Bootstrap(app)
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# limit upload size upto 8mb
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/', methods=['GET', 'POST'])
def index():
    model = ""
    if request.method == 'POST':
        image = request.files['car']
        image_path = pathlib.Path(app.config['UPLOAD_FOLDER'], secure_filename(image.filename)).as_posix()
        image.save(image_path)
        cropped = crop_image(image_path)
        print(cropped[0])
    return render_template('home.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)
