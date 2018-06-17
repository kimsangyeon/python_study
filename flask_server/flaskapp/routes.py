# routes
# -- coding: utf-8 --
import os
import sys
from flask import Flask, request, render_template
from werkzeug import secure_filename

app = Flask(__name__)
os.path.expanduser('~\\document')

@app.route("/")
def index():
    print(sys.prefix)
    return render_template("index.html")

@app.route("/getSerializedPbData", methods = ['POST', 'GET'])
def getSerializedPbData():
    if request.method == 'POST':
        f = request.files['docFile']
        f.save(os.path.abspath('~/') + secure_filename(f.filename))


if __name__ =='__main__':
    app.run(debug=True)