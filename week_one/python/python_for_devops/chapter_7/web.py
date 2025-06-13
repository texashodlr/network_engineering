from flask import Response, Flask
import prometheus_client

app = Flask('prometheus-app')

@app.route('/metrics/')
def metrics():
    return Response(
            prometheus_client.generate_latest(),
            mimetype='text/plain; version=0.0.4; charset=utf-8'
    )
