from flask import Flask, render_template, request, redirect
app = Flask(__name__)
expenses = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        description = request.form.get("description")
        amount = request.form.get("amount")
        if description and amount:
            try:
                amount = float(amount)
                expenses.append({"description": description, "amount": amount})
            except ValueError:
                pass  # Ignore invalid input
        return redirect("/")
    total = sum(item["amount"] for item in expenses)
    return render_template("index.html", expenses=expenses, total=total)

if __name__ == "__main__":
    app.run(debug=True)
