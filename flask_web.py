#!/usr/bin/env python
#coding=utf-8

import MySQLdb as mysql
import json
from flask import Flask, request, render_template
app = Flask(__name__)
db = mysql.connect(user="root", passwd="kop123",\
        db="falcon", charset="utf8")
db.autocommit(True)
c = db.cursor()
signined = False
@app.route("/", methods=["GET", "POST"])
def hello():
    sql = ""
    if request.method == "POST":
        data = request.json
        try:
            sql = "INSERT INTO `stat` (`host`,`mem_free`,`mem_usage`,`mem_total`,`load_avg`,`time`) VALUES('%s', '%d', '%d', '%d', '%s', '%d')" % (data['Host'], data['MemFree'], data['MemUsage'], data['MemTotal'], data['LoadAvg'], int(data['Time']))
            ret = c.execute(sql)
        except mysql.IntegrityError:
            pass
        return "OK"
    else:
        return render_template("mon.html")

@app.route("/data", methods=["GET"])
def getdata():
    c.execute("SELECT `time`,`mem_usage` FROM `stat`")
    ones = [[i[0]*1000, i[1]] for i in c.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))

@app.route("/signin",methods=['GET'])
def signin_form():
    return render_template('signin_form.html')

@app.route("/signin",methods=['POST'])
def signin():
    username = request.form['username']
    passwd = request.form['passwd']
    if username == 'admin' and passwd == 'qwer1234':
        signined = True
        return render_template('mon.html')
    signined = False
    return render_template('signin_form.html',message='Error user name or passwd!!',uname=username)

@app.route("/<name>",methods=["GET"])
def test(name):
    return render_template("test.html",name=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)