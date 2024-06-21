from flask import Blueprint, render_template, request, redirect, url_for
from models import Cause
from database import db

bp = Blueprint('causes', __name__)


@bp.route('/causes')
def causes():
    causes = Cause.query.all()
    return render_template('causes.html', causes=causes)


@bp.route('/causes/add', methods=['POST'])
def add_cause():
    title = request.form['title']
    description = request.form['description']
    new_cause = Cause(title=title, description=description)
    db.session.add(new_cause)
    db.session.commit()
    return redirect(url_for('causes.causes'))


@bp.route('/causes/<int:id>/edit', methods=['POST'])
def edit_cause(id):
    cause = Cause.query.get_or_404(id)
    cause.title = request.form['title']
    cause.description = request.form['description']
    db.session.commit()
    return redirect(url_for('causes.causes'))
