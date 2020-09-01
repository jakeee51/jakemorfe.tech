from flask import Flask, session, redirect, url_for, render_template,\
     request, make_response
from datetime import datetime
from GeoLiberator import parse_address
from gomaps import maps_search
from portfolio import application as app
from config import Config
from portfolio.tools import *
import json, time, re, os

if Config.RUN_MODE == "dev":
    print(">>>", os.path.basename(__file__))

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/index", methods=["GET", "POST"])
def index():
    return redirect(url_for('home'))

@app.route("/about_me", methods=["GET", "POST"])
def about_me():
    return render_template("about_me.html")

@app.route("/cv", methods=["GET", "POST"])
def cv():
    return render_template("cv.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

@app.route("/hire_me", methods=["GET", "POST"])
def hire_me():
    return render_template("hire_me.html")

@app.route("/twos_calc", methods=["POST"])
def twos_calc():
    if request.method == "POST":
        w = request.form["w"]
        op = request.form["arith"]
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        args = f"{w} {op} {num1} {num2}"
        resp = get_tca(args)
        return resp

@app.route("/GL", methods=["POST"])
def GL():
    if request.method == "POST":
        addr = request.form["addr"]
        parse = request.form["parse"]
        resp = parse_address(addr, parse)
        return resp

@app.route("/gmapi", methods=["POST"])
def gmapi():
    if request.method == "POST":
        place = request.form["place"]
        resp = maps_search(place)
        print(resp); print(list(resp), len(list(resp)))
        if len(list(resp)) == 1:
            return json.dumps(resp[0].get_values())
        else:
            lst = [str(obj) for obj in resp.list()]
            return json.dumps(lst)

@app.route("/projects", defaults={"project": None})
@app.route("/projects/<project>", methods=["GET", "POST"])
def projects(project):
    if project == None:
        return render_template("projects.html")
    else:
        return render_template(f"projects/{project}.html")
