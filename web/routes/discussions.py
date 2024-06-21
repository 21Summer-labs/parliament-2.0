from flask import Blueprint, render_template, request, redirect, url_for
from models import Discussion
from database import db

bp = Blueprint('discussions', __name__)


@bp.route('/discussions')
def discussions():
    discussions = Discussion.query.all()
    return render_template('discussions.html', discussions=discussions)


@bp.route('/discussions/add', methods=['POST'])
def add_discussion():
    title = request.form['title']
    content = request.form['content']
    new_discussion = Discussion(title=title, content=content)
    db.session.add(new_discussion)
    db.session.commit()
    return redirect(url_for('discussions.discussions'))


@bp.route('/discussions/<int:id>/update', methods=['POST'])
def update_discussion(id):
    discussion = Discussion.query.get_or_404(id)
    discussion.title = request.form['title']
    discussion.content = request.form['content']
    db.session.commit()
    return redirect(url_for('discussions.discussions'))


@bp.route('/discussions/<int:id>/like', methods=['POST'])
def like_discussion(id):
    discussion = Discussion.query.get_or_404(id)
    discussion.likes += 1
    db.session.commit()
    return redirect(url_for('discussions.discussions'))
