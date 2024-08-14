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

@app.route('/choose-desired-body/<age_group>/<body_type>/<goal>')
def choose_desired_body(age_group, body_type, goal):
    return render_template('choose_desired_body.html', age_group=age_group, body_type=body_type, goal=goal)

@app.route('/workout-plan/<age_group>/<body_type>/<goal>/<desired_body>')
def workout_plan(age_group, body_type, goal, desired_body):
    # This is where you'll generate the workout plan based on all parameters
    return f"Workout plan for age group {age_group}, body type {body_type}, goal {goal}, and desired body {desired_body}"

if __name__ == '__main__':
    app.run(debug=True)

    