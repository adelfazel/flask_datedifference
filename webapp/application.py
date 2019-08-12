import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.dateclass import DateClass
from flask import Flask, session, render_template, url_for, jsonify, request

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/getdiff",methods=["POST"])
def getdiff():
    try:
        Date1 = request.form.get("FD")
        Date2 = request.form.get("SD")
        print(f"Date1:{Date1}")
        print(f"Date2:{Date2}")
        Date1 = DateClass(Date1)
        Date2 = DateClass(Date2)
        diff = Date1.dayDifferece(Date2)
        return jsonify({"success":True, "Diff": diff})
    except TypeError as e:
        return jsonify({"success":False})
    except AttributeError as e:
        return jsonify({"success":False})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
