from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db
from ..functions import calculate_grades

grades = Blueprint('grades', __name__)

@grades.route('/grade', methods=['GET', 'POST'])
def grade():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new grade
    if request.method == 'POST':
        number_grade = request.form['number_grade']
        student_name = request.form['student_name']

        number_grade = int(number_grade)

        # call the calculate_grades function to get the letter grade
        letter_grade = calculate_grades([number_grade])

        # Insert the new grade info into the database
        cursor.execute('INSERT INTO student_grades (number_grade, letter_grade, student_name) VALUES (%s, %s, %s)', (number_grade, letter_grade, student_name))
        db.commit()
        return redirect(url_for('grades.grade'))

    # Handle GET request to display all grades
    cursor.execute('SELECT * FROM student_grades')
    all_grades = cursor.fetchall()
    return render_template('grades.html', all_grades=all_grades)

@grades.route('/update_grade/<int:grade_id>', methods=['GET', 'POST'])
def update_grade(grade_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the grade's details
        number_grade = request.form['number_grade']
        student_name = request.form['student_name']

        # call the calculate_grades function to get the letter grade
        letter_grade = calculate_grades([int(number_grade)])

        cursor.execute('UPDATE student_grades SET number_grade = %s, letter_grade = %s, student_name = %s WHERE grade_id = %s',
                       (number_grade, letter_grade, student_name, grade_id))
        db.commit()

        return redirect(url_for('grades.grade'))

    # GET method: fetch grade's current data for pre-populating the form
    cursor.execute('SELECT * FROM student_grades WHERE grade_id = %s', (grade_id,))
    current_grade = cursor.fetchone()
    return render_template('update_grade.html', current_grade=current_grade)

@grades.route('/delete_grade/<int:grade_id>', methods=['POST'])
def delete_grade(grade_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the grade
    cursor.execute('DELETE FROM student_grades WHERE grade_id = %s', (grade_id,))
    db.commit()
    return redirect(url_for('grades.grade'))