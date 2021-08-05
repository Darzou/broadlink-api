import os


class Config(object):
    DEBUG = True
    DEVELOPMENT = True

    CONTROLLERS = {
        "rmmini3_studio": (0x5f36, ("10.0.1.142", 80), "A043B04696B7")
    }

    IR_PACKETS = {
        "clim_studio": {
            "turn_on": """JgCSAAABJJEXNRc0FxEXNBcRFxAXERcQFzUXERcQFzUXEBcRFxAXERcQFxEXEBcRFxAYEBc0GBAX
                        ERcQFxEXEBc1FxAXNRcQGBAXNRcQFwACjRgQFxEXEBcRFxAXERYRFxEXNBcRFxAXERcQGBAXERcQ
                        FxEXEBcRFxAXERcQFxEXEBcRFxAXERcQFxEXNBg0FzUXAA0F"""
        }
    }

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
