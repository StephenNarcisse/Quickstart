from flask import Flask, render_template
import forms
from workouts import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "tempsecretkey"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    weight_form = forms.WeightForm()
    equip_form = forms.EquipmentChoice()
    days_form = forms.DaysChoice()
    lifts = forms.LiftingStatus()
    print(weight_form.bench_field.data, weight_form.press_field.data)
    print(weight_form.bench_field)

    return render_template("quiz.html",
                           weight_form=weight_form,
                           equip_form=equip_form,
                           days_form=days_form,
                           lifts=lifts
                           )


@app.route('/programs')
def programs():
    return render_template("programs.html", pl=powerlifting, bb=bodybuilding)


@app.route("/programs/<string:name>", methods=['GET', 'POST'])
def get_workout(name):
    weight_form = forms.WeightForm()
    print(weight_form.squat_field.data)
    bench = weight_form.bench_field.data
    press = weight_form.press_field.data
    squat = weight_form.squat_field.data
    deadlift = weight_form.deadlift_field.data

    return render_template(f"{name}.html",
                           weight_form=weight_form,
                           pl=powerlifting,
                           bb=bodybuilding,
                           tl=TEMPLATE,
                           )


if __name__ == "__main__":
    app.run(debug=True)
