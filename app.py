from flask import Flask, render_template
import ascii_arts as asciis


app = Flask(__name__)

coffee_done = False


@app.route("/")
def index():
    return render_template("teapot.html"), 418


@app.route("/teapot", methods=["GET"])
def teapot():
    return teapot_default()


@app.route("/teapot", methods=["BREW", "POST"])
def brew():
    return brew()


@app.route("/teapot", methods=["WHEN"])
def when():
    return when()


def teapot_default():
    global coffee_done
    if not coffee_done:
        return asciis.send_chilling(), 418
    elif coffee_done:
        coffee_done = False
        return asciis.send_coffee(), 418


def brew():
    return asciis.send_brewing(), 418


def when():
    global coffee_done
    coffee_done = True
    return asciis.send_pouring(), 418
