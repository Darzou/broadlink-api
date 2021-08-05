import logging
import broadlink
import binascii
from .exceptions import UnauthorizedAccess, ControllerNotFound, DeviceNotFound, \
    CommandNotFound, InvalidRequestBody

logger = logging.getLogger('api')


class BroadlinkApi():

    def __init__(self, flask_app):
        self._flask_app = flask_app

    def control_callback(self, controller_id, device_id, payload):
        try:
            if controller_id not in self._flask_app.config.get('CONTROLLERS'):
                raise ControllerNotFound("Controller %s not found." % controller_id)
            if device_id not in self._flask_app.config.get('IR_PACKETS'):
                raise DeviceNotFound("Device %s not found." % device_id)
            ctrl_cfg = self._flask_app.config.get('CONTROLLERS')[controller_id]
            packets = self._flask_app.config.get('IR_PACKETS')[device_id]

            # Get the broadlink device
            device = broadlink.gendevice(ctrl_cfg[0], ctrl_cfg[1], ctrl_cfg[2])

            if not isinstance(payload, dict):
                raise InvalidRequestBody("Invalid request body.")
            if payload.get('command', None) is None or packets.get(payload['command'], None) is None:
                raise CommandNotFound("Available commands: %s" % list(packets.keys()))

            hex_packet = packets[payload['command']]

            logger.info('Controlling %s via %s: %s', device_id, controller_id, payload['command'])
            device.auth()
            device.send_data(binascii.unhexlify(hex_packet))
        except Exception as e:
            logger.error("(%s): %s" % (e.__class__.__name__, e))
            return "(%s): %s" % (e.__class__.__name__, e), 400
        else:
            return 'success', 200
