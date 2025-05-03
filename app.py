from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# allows to access data on different addresses
app = Flask(__name__)
CORS(app)

# sqlalchemy configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)


# ------------------------
# Database Model
# -------------------------


class Finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(20), nullable=False)
    expense = db.Column(db.Float, nullable=False)


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


# This route renders the index.html
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# This route handles the POST request from the expense-form in index.html
@app.route("/", methods=["POST"])
def get_expense():
    data = request.json
    month = data.get("month")
    expense = data.get("expense")

    if (
        month not in valid_months
        and month not in short_valid_months
        or not isinstance(expense, (int, float))
    ):
        return jsonify({"error": "Invalid Input"}), 400

    # Save to DB instead of a dictionary
    new_expense = Finance(month=month, expense=expense)
    db.session.add(new_expense)
    db.session.commit()

    return jsonify({"message": f"{expense} added to {month}."})


@app.route("/summary", methods=["GET"])
def summary():
    all_data = Finance.query.all()
    summary_data = {}
    total = 0

    for item in all_data:
        if item.month in summary_data:
            summary_data[item.month] += item.expense
        else:
            summary_data[item.month] = item.expense
        total += item.expense

    return jsonify({"summary": summary_data, "total": total})


# This new route is necessary to separate the concerns, summary for data only, and summary page for html purely for presentation
@app.route("/summary_page", methods=["GET"])
def summary_page():
    return render_template("summary.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
