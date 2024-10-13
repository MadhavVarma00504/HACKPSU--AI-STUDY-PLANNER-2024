from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

# Create the database within the application context
with app.app_context():
    db.create_all()

# Route for home page
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# Route for adding a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    deadline = request.form['deadline']
    duration = request.form['duration']
    new_task = Task(task_name=task_name, deadline=deadline, duration=duration)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'task_name': task_name, 'deadline': deadline, 'duration': duration})

# Route to set free time and get AI-based recommended times
@app.route('/set_free_time', methods=['POST'])
def set_free_time():
    free_time_start = int(request.form['free_time_start'])
    free_time_end = int(request.form['free_time_end'])
    
    # Simple AI-based recommendation
    recommended_times = []
    for hour in range(free_time_start, free_time_end):
        recommended_times.append({
            'time': f'{hour}:00',
            'productivity_score': f'{(hour * 1.5) % 10:.2f}'  # Simple score for demo
        })
    return jsonify(recommended_times)

if __name__ == "__main__":
    app.run(debug=True)
