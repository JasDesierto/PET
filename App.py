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


if __name__ == "__main__":
    app.run(debug=True)
