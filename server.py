"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template
import hackbright

app = Flask(__name__)


@app.route('/student')
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template('student_info.html', first_name=first, last_name=last, github_user=github)


@app.route('/search')
def search():
    return render_template('student_search.html')


# @app.route('/add_student', methods=['POST'])
@app.route('/add_student')
def add_student():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    github = request.form.get("github")

    first_name, last_name, github = hackbright.make_new_student(first_name, last_name, github)

    return render_template('student_creation.html')


if __name__ == '__main__':
    hackbright.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
