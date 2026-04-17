from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def result15():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        date = request.form.get("date")



        return render_template("result15.html", name=name, phone=phone, email=email, date=date)

    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
