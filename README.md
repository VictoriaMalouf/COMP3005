# COMP3005

## Overview
Python-based application that connects to a database to perform specific CRUD (Create, Read, Update, Delete) operations.

## Setup Instructions
1. Clone the repository 
    - git clone `git@github.com:VictoriaMalouf/COMP3005.git`
2. Create a virtual environment
    - `python3 -m venv venv`
3. Install requirements
    - `pip-compile requirements.in`
    - `pip install -r requirements.txt`
4. Navigate to: src > application
   
   **help**:

      `python3 students.py -h`
      
   **getAllStudents()**:
    
      `python3 students.py -get`
      
   **addStudent(first_name, last_name, email, enrollment_date)**:

      `python3 students.py --add Selena Gomez sg@gmail.com '2024-03-12'`
      
   **updateStudentEmail(student_id, new_email)**:

      `python3 students.py -get`

## Link to Demonstration Video
https://youtu.be/nGL0doGFqWM
