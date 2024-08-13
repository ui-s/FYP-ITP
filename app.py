from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/body-type/<age_group>')
def body_type(age_group):
    return render_template('body_type.html', age_group=age_group)

@app.route('/workout-plan/<age_group>/<body_type>')
def workout_plan(age_group, body_type):
    # This is where you'll generate the workout plan based on age and body type
    return f"Workout plan for age group {age_group} and body type {body_type}"

if __name__ == '__main__':
    app.run(debug=True)