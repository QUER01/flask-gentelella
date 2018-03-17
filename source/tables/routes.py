from flask import Blueprint, render_template
from flask_login import login_required
from database import db
from base.models import data_table_1
from base.models import data_table_2


blueprint = Blueprint(
    'tables_blueprint',
    __name__,
    url_prefix='/tables',
    template_folder='templates',
    static_folder='static'
)


@blueprint.route('/<template>')
@login_required
def route_template(template):
    data_from_table_1 = [i for i in data_table_1.query.all()]
    data_from_table_2 = [i for i in data_table_2.query.all()]
    # data for chart
    legend = 'Monthly Data'
    labels = []
    values = []



    for u in data_table_1.query.all():
        print(u.name, u.value1)
        values.append(u.value1)
        labels.append(u.name)

    print(labels,values)
    return render_template(template + '.html'
                           ,data_from_table_1 = data_from_table_1
                           ,data_from_table_2 = data_from_table_2
                           ,values=values, labels=labels, legend=legend
                           )





