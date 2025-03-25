from flask import Flask,render_template,request
from datetime import datetime, timezone, timedelta

#from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():#這邊可以做成列表式
    homepage = "<h1>林冠廷Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=Linc&c=PU4B>傳送使用者暱稱</a><br>"
    homepage += "<a href=/account>網頁表單傳值</a><br>"
    homepage += "<a href=/about>林冠廷簡介網頁</a><br>"
    return homepage

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    c = request.values.get("c")

    return render_template("welcome.html", name=user,pu=c)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method=="POST":
        user = request.form["user"]
        pwd  = request.form['pwd']
        result="您輸入的帳號是："+user+"密碼為："+pwd
        return result
    else:    
        return render_template("account.html")
    



if __name__ == "__main__":
    app.run()
    #serve(app,host='0.0.0.0',port=8080)
