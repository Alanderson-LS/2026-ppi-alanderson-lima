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
            error = 'O problema precisa de um título.'
        elif not statement:
            error = 'O problema precisa de um enunciado.'
        elif not difficulty:
            error = 'O problema precisa de uma dificuldade.'
        elif not answer:
            error = 'O problema precisa de uma resposta.'
        elif not subject:
            error = 'O problema precisa de um conteudo.'

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

def get_problem(id, check_author=True):
    problem = get_db().execute(
        'SELECT p.id, title, statement, created, author_id, username, subject, difficulty, answer, resolution'
        ' FROM problem p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if problem is None:
        abort(404, f"Problem id {id} doesn't exist.")

    if check_author and problem['author_id'] != g.user['id']:
        abort(403)

    return problem

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    problem = get_problem(id)

    if request.method == 'POST':
        title = request.form['title']
        statement = request.form['statement']
        difficulty = request.form['difficulty']
        answer = request.form['answer']
        subject = request.form['subject']
        resolution = request.form['resolution']
        error = None

        if not title:
            error = 'O problema precisa de um título.'
        elif not statement:
            error = 'O problema precisa de um enunciado.'
        elif not difficulty:
            error = 'O problema precisa de uma dificuldade.'
        elif not answer:
            error = 'O problema precisa de uma resposta.'
        elif not subject:
            error = 'O problema precisa de um conteudo.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE problem SET title = ?, statement = ?, difficulty = ?, answer = ?, subject = ?, resolution = ?'
                ' WHERE id = ?',
                (title, statement, difficulty, answer, subject, resolution, id)
            )
            db.commit()
            return redirect(url_for('problem.index'))

    return render_template('problem/update.html', problem=problem)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_problem(id)
    db = get_db()
    db.execute('DELETE FROM problem WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('problem.index'))
