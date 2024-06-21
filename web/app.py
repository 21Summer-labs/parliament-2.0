import os
from flask import Flask, render_template
from database import db
from routes import bills, causes, discussions, communities
from models import Bill, Cause, Discussion

app = Flask(__name__)

# Ensure the instance folder exists
if not os.path.exists('instance'):
    os.makedirs('instance')

# Use absolute path for the database file
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'instance', 'parliament.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register blueprints
app.register_blueprint(bills.bp)
app.register_blueprint(causes.bp)
app.register_blueprint(discussions.bp)
app.register_blueprint(communities.bp)


@app.route('/')
def home():
    latest_bills = Bill.query.order_by(Bill.id.desc()).limit(5).all()
    top_discussions = Discussion.query.order_by(
        Discussion.likes.desc()).limit(5).all()
    featured_causes = Cause.query.limit(3).all()

    return render_template('home.html',
                           latest_bills=latest_bills,
                           top_discussions=top_discussions,
                           featured_causes=featured_causes)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
