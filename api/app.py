from flask import Flask, render_template, request, re
app = Flask(__name__)


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/")
def hello_world():
    return render_template("index.html")


def process_query(query):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"

    if query == "asteroids":
        return "Unknown"

    if query == "What is your name?":
        return "team"

    pattern = r'What is (\d+) plus (\d+)?'
    match = re.match(pattern, query)
    if match:
        first_number = int(match.group(1))
        second_number = int(match.group(2))
        return first_number + second_number
    else:
        raise ValueError("Query format not recognized")


@app.route("/query", methods=["GET"])
def handle_query():
    query_query = request.args.get('q')
    return process_query(query_query)
