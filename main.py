from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from form import AddForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
db = SQLAlchemy()
db.init_app(app)
Bootstrap5(app)


def check(yes_or_no):
    if yes_or_no == "YES":
        return True
    else:
        return False


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all-cafe")
def all_cafe():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.id))
    cafes = result.scalars()
    return render_template("all_cafe.html", cafes=cafes)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        print(form.has_toilet.data)
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            seats=form.seats.data,
            has_toilet=check(form.has_toilet.data),
            has_wifi=check(form.has_wifi.data),
            has_sockets=check(form.has_sockets.data),
            can_take_calls=check(form.can_take_calls.data),
            coffee_price=form.coffee_price.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


@app.route("/delete/<int:cafe_id>")
def delete(cafe_id):
    cafe_to_del = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    db.session.delete(cafe_to_del)
    db.session.commit()
    return redirect(url_for('all_cafe'))


if __name__ == "__main__":
    app.run(debug=True)
