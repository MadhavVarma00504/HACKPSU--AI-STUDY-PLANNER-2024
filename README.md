# HACKPSU--AI-STUDY-PLANNER-2024



AI-Powered Study Planner
An intelligent study scheduling tool that helps students manage their tasks and optimize their study time based on available free time and predicted productivity. This tool provides AI-based recommendations for study times to enhance productivity.

Features
Task Management: Add tasks with a name, deadline, and duration. Tasks are stored and displayed in "Your Study Schedule."
Free Time Input: Set your available free time for the day, which the AI uses to generate recommended study times.
AI-Based Study Recommendations: After setting available free time, the AI provides time slots with associated productivity scores, helping users choose the best study hours.
Progress Tracking: Visualize and track tasks in the "Your Study Schedule" section.
Responsive UI: Clean and user-friendly interface designed for an optimal user experience.


Technology Stack
Backend: Flask (Python)
Frontend: HTML, CSS, JavaScript (Bootstrap for styling)
Database: SQLite (via SQLAlchemy ORM)
Machine Learning: Simple AI-based recommendation engine using hardcoded productivity scores based on available time.
Interactive Elements: Interactive forms to input tasks and free time, and dynamic display of study recommendations.


Installation
Prerequisites
Make sure you have the following installed:

Python 3.x
Flask
SQLAlchemy
Step-by-Step Guide
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo-url/ai-powered-study-planner.git
cd ai-powered-study-planner


Install dependencies:

Copy code
pip install flask flask_sqlalchemy
Run the app:

Copy code
python app.py
Open the app in your browser:

arduino
Copy code
http://127.0.0.1:5000

Usage
Add New Task:

Fill in the task name, select a deadline, and specify the duration in hours.
After clicking "Add Task", the task will appear under "Your Study Schedule."

Set Available Free Time:

Input the start and end of your available free time in the day (from 1 to 12 hours).
Click "Set Free Time" to generate AI-based recommended study times. The recommended times and their corresponding productivity scores will be displayed under "Recommended Study Times."
Study Recommendations:

The AI-based recommendations help you choose the best hours to study based on predicted productivity scores.

File Structure
graphql
Copy code
.
├── app.py                 # Main Flask application
├── templates
│   └── index.html         # HTML template for the UI
├── static
│   ├── style.css          # Custom CSS for UI design
│   └── main.js            # JavaScript for client-side interactivity (if applicable)
├── tasks.db               # SQLite database (auto-generated)
└── README.md              # This readme file

Future Enhancements
Advanced AI Model: Integrate a more sophisticated AI model to predict productivity based on user study patterns and preferences.
Real-Time Calendar Integration: Add a calendar where tasks and recommended study times can be visualized.
Progress Tracking: Implement a progress bar or chart that dynamically updates based on completed tasks.
Task Reminders: Add an alert or reminder system to notify users about their scheduled study times.


Challenges Faced
Managing application contexts for database operations in Flask.
Ensuring smooth integration of task scheduling and study time recommendations.
Creating a simple yet effective AI-based recommendation system.
