from flask import Blueprint, render_template
from models import Community

bp = Blueprint('communities', __name__)


@bp.route('/communities')
def communities():
    communities = Community.query.all()
    return render_template('communities.html', communities=communities)
