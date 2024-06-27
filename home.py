from flask import Flask,request
user = "Samuel"
def login_form():
    return """
<p>Welcome {0}, to our python home page</p>
<form>
<input type="text"><br><br>
<input type="text"><br><br>
<input type="button"><br><br>
</form>
""".format(user)

app = Flask(__name__)
@app.route("/",methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        return "d"
    else:
        return login_form()


@app.route("/profile")
def profile():
    return "profile page"