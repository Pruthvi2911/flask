from flask import flask,render_template
name=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/education")
def home():
    return render_template("education.html")


@app.route("/experience")
def home():
    return render_template("experience.html")


@app.route("/projects")
def home():
    return render_template("projects.html")


@app.route("/writetome")
def home():
    return render_template("writetome.html")



if __name__=='__main__':
    app.run(debug=True)

