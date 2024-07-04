from flask import Flask, render_template, request
import ascii_arts as asciis


app = Flask(__name__)

coffee_done = False
user_agent = request.headers.get('User-Agent')


@app.route("/")
def index():
    return render_template("teapot.html"), 418


@app.route("/teapot", methods=["GET"])
def teapot():
    global coffee_done
    if not coffee_done:
        if 'curl' in user_agent:
            return asciis.send_chilling(), 418
        else:
            return render_template("teapot.html"), 418
    elif coffee_done:
        coffee_done = False
        if 'curl' in user_agent:
            return asciis.send_coffee(), 418
        else:
            return render_template("coffee.html"), 418


@app.route("/teapot", methods=["BREW", "POST"])
def brew():
    global coffee_done
    coffee_done = True
    if 'curl' in user_agent:
        return asciis.send_brewing(), 418
    else:
        return render_template("brewing.html"), 418


@app.route("/teapot", methods=["WHEN"])
def when():
    if 'curl' in user_agent:
        return asciis.send_pouring(), 418
    else:
        return render_template("pouring.html"), 418
