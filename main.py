from flask import Flask, render_template, request
from datetime import datetime
from scrapp import scrape_stocks, scrape_pm25

# print(__name__)

app = Flask(__name__)

books = {
    1: {
        "name": "Python book",
        "price": 299,
        "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348",
    },
    2: {
        "name": "Java book",
        "price": 399,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348",
    },
    3: {
        "name": "C# book",
        "price": 499,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348",
    },
}


@app.route("/pm25", methods=["GET", "POST"])
def get_pm25():
    # GET
    print(request.args)
    # POST
    print(request.form)
    today = datetime.now()

    sort = False
    ascending = True

    if request.method == "POST":
        # 判斷是否按下排序按鈕
        if "sort" in request.form:
            sort = True
            # 取得select的option
            ascending = True if request.form.get("sort") == "true" else False

    columns, values = scrape_pm25(sort, ascending)
    data = {
        "columns": columns,
        "values": values,
        "today": today.strftime("%Y/%m/%d %H:%M:%S"),
    }
    return render_template("pm25.html", data=data)


@app.route("/stocks")
def get_stocks():
    datas = scrape_stocks()

    # for data in datas:
    #     print(data[0], data[1])
    return render_template("stocks.html", datas=datas)


@app.route("/bmi/name=<name>&height=<height>&weight=<weight>")
def get_bmi(name, height, weight):
    try:
        bmi = round(eval(weight) / (eval(height) / 100) ** 2, 2)
        return f"{name} BMI:{bmi}"
    except Exception as e:
        print(e)

    return "<h1>參數不正確!</h1>"


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
    print(books)

    for key in books:
        print(books[key])

    return render_template("books.html", books=books)


@app.route("/")
def index():
    today = datetime.now()
    print(today)
    name = "jerry"
    # return f"<h1>HI Flask!<br>{x+y}<br>{today}</h1>"
    return render_template("index.html", date=today, name=name)


app.run(debug=True)
