from flask import Blueprint, render_template, request, redirect, url_for
from models import Bill
from database import db

bp = Blueprint('bills', __name__)


@bp.route('/bills')
def bills():
    bills = Bill.query.all()
    return render_template('bills.html', bills=bills)


@bp.route('/bills/add', methods=['POST'])
def add_bill():
    title = request.form['title']
    description = request.form['description']
    new_bill = Bill(title=title, description=description)
    db.session.add(new_bill)
    db.session.commit()
    return redirect(url_for('bills.bills'))


@bp.route('/bills/<int:id>/vote')
def bill_vote(id):
    bill = Bill.query.get_or_404(id)
    options = ["Jomo Kenyatta", "Daniel arap Moi",
               "Mwai Kibaki", "Uhuru Kenyatta", "William Ruto"]
    return render_template('bill_vote.html', bill=bill, options=options)
