from flask import Flask, render_template, request, redirect, url_for
from controllers.claim_controller import ClaimController
from model.database import init_db

app = Flask(__name__)
controller = ClaimController()

init_db()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        role = request.form["role"]
        if role == "citizen":
            return redirect("/claim")
        elif role == "staff":
            return redirect("/claims")
    return render_template("login.html")


@app.route("/claim", methods=["GET", "POST"])
def create_claim():
    if request.method == "POST":
        amount, calc_date = controller.create_claim_web(request.form)
        return render_template("claim_form.html", amount=amount, calc_date=calc_date)
    return render_template("claim_form.html")


@app.route("/claims")
def list_claims():
    claims = controller.list_claims_web()
    return render_template("claim_list.html", claims=claims)


if __name__ == "__main__":
    app.run(debug=True)
