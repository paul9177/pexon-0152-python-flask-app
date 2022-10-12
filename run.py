# coding=utf-8
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    # items = ["Apfel", "Birne", "Banane"]
    items = [
    "Cloud",
    "Practitioner",

    "Solutions",
    "Architekt",
    "Developer",
    "SysOps",
    "Administrator",

    "Solution",
    "Architekt",
    "DevOps",
    "Engineer",

    "Advanced",
    "Networking",
    "Data",
    "Analytics",
    "Database",
    "Machine",
    "Learning",
    "Security",
    "SAP",
    "on",
    "AWS"]

    return render_template("start.html", name="Meiene Zertifizierungen", items=items)

@app.route("/test")
def test():
    name = request.args.get("name")
    age = request.args.get("age")

    # return scheint hier die view zu sein
    return render_template("test.html", name=name, age=age) # variablen inhalt an view weitergeben


