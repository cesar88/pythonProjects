from flask import Flask,render_template,request
import requests
from instagram_parser import instagram_lib

app = Flask(__name__)


@app.route('/', methods={"POST","GET"})
def hello_world():
    if request.method=="POST":
        user_name=request.form["username"]
        instagram_data=instagram_lib(user_name)
        return render_template("img_show.html",instagram_data=instagram_data)

    return render_template("index.html")

@app.route('/download', methods={"POST","GET"})
def download():
    if request.method == "POST":
        return  request.form["indir"]




if __name__ == '__main__':
    app.run()
