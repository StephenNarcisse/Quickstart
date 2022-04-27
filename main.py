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
    print(weight_form.bench_field, weight_form.press_field)
    lifts = forms.LiftingStatus()
    return render_template("quiz.html",
                           weight_form=weight_form,
                           equip_form=equip_form,
                           days_form=days_form,
                           bench=weight_form.bench,
                           press=weight_form.press,
                           squat=weight_form.squat,
                           deadlift=weight_form.deadlift,
                           lifts=lifts
                           )

@app.route('/programs')
def programs():

    return render_template("programs.html", pl=powerlifting)


@app.route("/programs/<string:name>")
def get_workout(name):
    return render_template("workout.html")


if __name__ == "__main__":
    app.run(debug=True)
