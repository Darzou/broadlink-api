from app import app, api
from flask import request


@app.route('/control/<controller_id>/<device_id>', methods=['POST'])
def post_control(controller_id, device_id):
    payload = request.get_json()

    return api.control_callback(controller_id, device_id, payload)
