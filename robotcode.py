from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/robotcode/go/<feet>')
def straight(feet=None):
	seconds = int(feet) * 1000
	return render_template('code.html', feet=feet, seconds=seconds)

@app.route('/robotcode/square/<feet>')
def square(feet=None):
	seconds = int(feet) * 1000
	return render_template('squarecode.html', feet=feet, seconds=seconds)

if __name__ == '__main__':
    app.run(debug=True)