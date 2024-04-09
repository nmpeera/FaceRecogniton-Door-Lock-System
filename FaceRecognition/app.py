from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/face_recognition/')
def face_recognition():
	return os.system('python face_recognition.py')

@app.route('/DataSet/')
def DataSet():
	return os.system('python face_dataset.py')

@app.route('/Delete/')
def Delete():
	return os.system('python face_delete.py')

if __name__ == '__main__':
	app.run(debug=True)
#, host='0.0.0.0', port=5000
