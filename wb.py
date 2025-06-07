from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/',methods=['GET'  ])
def index():

    return render_template("wb.html")

@app.route('/get')
def get():
    return render_template("get.html")


@app.route('/mycss')
def mycss():
    return render_template("mycss.html")


@app.route('/sousuo',methods=['GET'])
def sousuo():
    print(request.args)
    return  "提交成功"


@app.route('/denglu',methods=['POST'])
def denglu():
    print(request.form)
    return  "提交成功"

if __name__ == '__main__':
    app.run(debug=True )