from flask import Flask, render_template, request, session
from apiget import *
from datareset import *
import pprint

app = Flask(__name__)


@app.before_request

def before_request():
    session.modified = False
#question_index = session.get("q_index", 0)
question_index = 0
user_answers = []


response = api_start()
questions = response["results"]
new_data = restructure(response)


@app.route("/", methods=["GET","POST"])
def hello_world():
    global question_index, user_answers
    #pprint.pprint(new_data)
    if request.method == "POST":
        selected_option = request.form.get("option")
        user_answers.append(selected_option)
        question_index += 1
    if question_index >= len(new_data):
        score = calc_score(new_data, user_answers)
        question_index = 0
        user_answers = []
        return render_template("results.html", score=score)
    current_question = new_data[question_index]
    
    return render_template("index.html",api_data=new_data, count=question_index)


