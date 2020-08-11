from flask import Flask, session, redirect, url_for, render_template,\
     request, make_response
from datetime import datetime
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

@app.route("/projects", methods=["GET", "POST"])
def projects():
    return render_template("projects.html")

@app.route("/cv", methods=["GET", "POST"])
def cv():
    return render_template("cv.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

@app.route("/hire_me", methods=["GET", "POST"])
def hire_me():
    return render_template("hire_me.html")
