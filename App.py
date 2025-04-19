from flask import Flask, request, jsonify
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
    "Jul",
    "Aug",
    "Sept",
    "Oct",
    "Nov",
    "Dec",
]


@app.route("/", methods=["POST"])
def get_expense():

    data = request.json
    month = data.get("month")
    expense = data.get("expense")

    if (
        month not in valid_months
        or short_valid_months
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
@app.route("/summary_page", methods={"GET"})
def summary_page():
    return render_template("summary.html")


if __name__ == "__main__":
    app.run(debug=True)
