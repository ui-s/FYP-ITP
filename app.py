from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/body-type/<age_group>')
def body_type(age_group):
    return render_template('body_type.html', age_group=age_group)

@app.route('/choose-goal/<age_group>/<body_type>')
def choose_goal(age_group, body_type):
    return render_template('choose_goal.html', age_group=age_group, body_type=body_type)

@app.route('/workout-plan/<age_group>/<body_type>/<goal>')
def workout_plan(age_group, body_type, goal):
    # This is where you'll generate the workout plan based on age, body type, and goal
    return f"Workout plan for age group {age_group}, body type {body_type}, and goal {goal}"

if __name__ == '__main__':
    app.run(debug=True)