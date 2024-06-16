from flask import render_template

from .blueprint import user_blueprint


@user_blueprint.route("/top-up", methods=["GET", "POST"])
def top_up_credit():
    return render_template("views/top_up_credit.html")
