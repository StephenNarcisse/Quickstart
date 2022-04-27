from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired


# Create a Form Class
class NamerForm(FlaskForm):
    name = fields.StringField("What's your name")
    submit = fields.SubmitField("Submit")


class LiftingStatus(FlaskForm):
    radio = fields.RadioField("Lifting Status", choices=["Beginner", "Intermediate"])


class EquipmentChoice(FlaskForm):
    equipment = fields.SelectField("Available Equipment: ", choices=["None", "Barbell", "Dumbbell", "Both", "Gym"])


class DaysChoice(FlaskForm):
    radio = fields.RadioField("Days Per Week: ", choices=["2","3", "4", "5", "6"])


class WeightForm(FlaskForm):
    bench = press = squat = deadlift = 0
    bench_field = fields.IntegerField("Bench Press")
    press_field = fields.IntegerField("Overhead Press")
    squat_field = fields.IntegerField("Squat")
    deadlift_field = fields.IntegerField("Deadlift")
