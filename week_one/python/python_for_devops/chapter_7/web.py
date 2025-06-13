import time
import random
from flask import Response, Flask
import prometheus_client
from prometheus_client import Counter, Histogram

"""
Access the site on http://localhost:5000
Access metrics via ...5000/metrics/
Access the splash via 5000/
Access the DB fail via 5000/database/

"""

app = Flask('prometheus-app')

REQUESTS = Counter(
        'requests', 'Application Request Count',
        ['endpoint']
    )
TIMER = Histogram(
        'slow', 'Slow Requests',
        ['endpoint']
    )

@app.route('/database/')
def database():
    with TIMER.labels('/database').time():
        # Simulated DB response time
        sleep(random.uniform(1, 3))
    return '<h1>Completed expensive database operations</h1>'

@app.route('/')
def index():
    REQUESTS.labels(endpoint='/').inc()
    return '<h1>Development Prometheus-backed Flask App</h1>'

@app.route('/metrics/')
def metrics():
    return Response(
            prometheus_client.generate_latest(),
            mimetype='text/plain; version=0.0.4; charset=utf-8'
    )
