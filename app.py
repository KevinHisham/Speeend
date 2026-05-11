import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'sqlite:///speeend.db'
)

db = SQLAlchemy(app)


class Expense(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    amount     = db.Column(db.Float, nullable=False)
    category   = db.Column(db.String(50), nullable=False)
    note       = db.Column(db.String(200))
    date       = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

with app.app_context():
    db.create_all()


# Endpoint 1 - Beranda
@app.route("/")
def home():
    return """
    <h1>Speeend</h1>
    <p>Aplikasi pencatat pengeluaran harian</p>
    """


# Endpoint 2 - Health check
@app.route("/health")
def health():
    return jsonify({'status': 'sehat'})


# Endpoint 3 - Tambah pengeluaran
@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.get_json()

    if not data or not data.get("amount") or not data.get("category"):
        return jsonify({"error": "amount dan category wajib diisi"}), 400

    expense = Expense(
        amount=data["amount"],
        category=data["category"],
        note=data.get("note", ""),
        date=data.get("date", datetime.utcnow().strftime("%Y-%m-%d"))
    )
    db.session.add(expense)
    db.session.commit()

    return jsonify({"message": "Pengeluaran berhasil ditambahkan", "id": expense.id}), 201


# Endpoint 4 - Lihat semua pengeluaran
@app.route("/expenses", methods=["GET"])
def get_expenses():
    expenses = Expense.query.order_by(Expense.created_at.desc()).all()
    return jsonify([{
        "id": e.id,
        "amount": e.amount,
        "category": e.category,
        "note": e.note,
        "date": e.date
    } for e in expenses])


# Endpoint 5 - Ringkasan per kategori
@app.route("/expenses/summary", methods=["GET"])
def summary():
    expenses = Expense.query.all()
    result = {}
    for e in expenses:
        result[e.category] = result.get(e.category, 0) + e.amount

    return jsonify({
        "total": sum(result.values()),
        "per_kategori": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)