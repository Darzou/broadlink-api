import broadlink

devices = broadlink.discover(timeout=5)

print("Discovered devices: %s" % devices)
