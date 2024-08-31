from flask import Flask
from datetime import datetime

# print(__name__)

app = Flask(__name__)

books = {1: "Python book", 2: "Java book", 3: "Flask book"}


@app.route("/bmi/name=<name>&height=<height>&weight=<weight>")
def get_bmi(name, height, weight):
    bmi = round(eval(weight) / (eval(height) / 100) ** 2, 2)
    return f"{name} BMI:{bmi}"


@app.route("/sum/x=<x>&y=<y>")
def my_sum(x, y):
    # 參數不正確，請輸出參數錯誤 (try + except)
    try:
        total = eval(x) + eval(y)
        return f"<h2>{x}+{y}={total}</h2>"
    except Exception as e:
        print(e)

    return "<h2>參數不正確!</h2>"


@app.route("/book/<int:id>")
def show1_book(id):
    # 輸出有書 <h1>第一本書:XXX</h1>
    # 無此編號
    if id not in books:
        return f"<h2 style='color:red'>無此編號:{id}</h2>"

    return f"<h1>第{id}本書:{books[id]}</h1>"


@app.route("/books")
def show_books():
    return books


@app.route("/")
def index():
    today = datetime.now()
    print(today)
    x = 10
    y = 20
    return f"<h1>HI Flask!<br>{x+y}<br>{today}</h1>"


app.run(debug=True)
