
# Student Name: Krzysztof Bas
# Student Number: C00238768

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_page():
    title = "Home"
    bob = "Welcome explorer, don't forget to leave a comment   :) ."
    thank_you_msg = "Thank you for your comment :) "

    data = request.form
    if request.method == "POST":
        with open("comments.txt", "a") as commentFile:
            print(data["email"], end=", '", file=commentFile)
            print(data["comment"], end="'\n\n", file=commentFile)

        return render_template(
            "home.html", the_title=title, bobek=bob, ty_msg=thank_you_msg
        )

    return render_template("home.html", the_title=title, bobek=bob)


@app.route("/personalPage")
def personal_page():
    title = "About Me"
    return render_template("personalPage.html", the_title=title)


@app.route("/cv")
def cv_page():
    title = "Curriculum vitae"
    return render_template("cv.html", the_title=title)


@app.route("/tech1")
def tech1_page():
    title = "Python"
    return render_template("tech1.html", the_title=title)


@app.route("/tech2")
def tech2_page():
    title = "Gaming"
    return render_template("tech2.html", the_title=title)


@app.route("/tech3")
def tech3_page():
    title = "Algorithms"
    return render_template("tech3.html", the_title=title)


@app.route("/interests")
def interests_page():
    title = "Interests"
    return render_template("interests.html", the_title=title)


if __name__ == "__main__":
    app.run(debug=True)
