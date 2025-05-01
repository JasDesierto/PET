from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

finances = {}

valid_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

short_valid_months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]


# ? Added this route to render the index.html file using flask
@app.route("/", methods=["GET"])
def index():
    # ? you need "render_template" to render the index.html file
    # ? go to http://127.0.0.1:5000/ to on your browser to see home page
    # ? do this instead of using vs code's live preview extension
    return render_template("index.html")


# ! This route is not used to render the index.html file
# ? This route handles the POST request from the expense-form in index.html
# ? that was sent by the script.js file when the form is submitted
@app.route("/", methods=["POST"])
def get_expense():
    data = request.json
    month = data.get("month")
    expense = data.get("expense")

    if (
        month not in valid_months
        and month not in short_valid_months  # ? better logic to check for short months
        or not isinstance(expense, (int, float))
    ):
        return jsonify({"error": "Invalid Input"}), 400

    if month in finances:
        finances[month] += expense
    else:
        finances[month] = expense

    return jsonify({"message": f"{expense} added to {month}."})


@app.route("/summary", methods=["GET"])
def summary():
    total = sum(finances.values())
    return jsonify({"summary": finances, "total": total})


# This new route is necessary to separate the concerns, summary for data only, and summary page for html purely for presentation
@app.route("/summary_page", methods=["GET"])
def summary_page():
    return render_template("summary.html")


if __name__ == "__main__":
    app.run(debug=True)
