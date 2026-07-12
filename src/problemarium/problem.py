from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db

bp = Blueprint('problem', __name__)

@bp.route('/')
def index():
    db = get_db()
    problems = db.execute(
        'SELECT p.id, title, created, author_id, username, statement, subject, difficulty, answer, resolution'
        ' FROM problem p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('problem/index.html', problems=problems)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        statement = request.form['statement']
        difficulty = request.form['difficulty']
        answer = request.form['answer']
        subject = request.form['subject']
        resolution = request.form['resolution']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO problem (title, statement, author_id, difficulty, answer, subject, resolution)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?)',
                (title, statement, g.user['id'], difficulty, answer, subject, resolution)
            )
            db.commit()
            return redirect(url_for('problem.index'))

    return render_template('problem/create.html')
