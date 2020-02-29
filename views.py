import json


from models import LogRecord
from app import app
from flask import render_template
from sqlalchemy import text


@app.route('/')
def home():
    records = LogRecord.query.all()

    data = {}
    for r in records:
        if r.log_type not in data:
            data[r.log_type] = []

        data[r.log_type].append({
            'value': r.value,
            'time': r.timestamp,
        })

    return render_template('home.html', chart_data=json.dumps(data))
