from flask import Flask, render_template

application = Flask(__name__)


@application.route('/Home/')
def home():
	return render_template("home.html")


@application.route('/Projects/')
def projects():
	return render_template("projects.html")


@application.route('/About/')
def about():
	return render_template("about.html")


if __name__ == '__main__':
	application.run(debug=True)
