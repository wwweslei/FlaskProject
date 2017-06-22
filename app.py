from flask import Flask, render_template, request


app = Flask("FlaskProject")
app.debug = True


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("test.html", result=result)


if __name__ == '__main__':
    app.run()
 