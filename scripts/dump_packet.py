import broadlink
import time
import binascii


devices = broadlink.discover(timeout=5)
device = devices[0]
device.auth()
device.enter_learning()

packet = None

print("Learning", end="", flush=True)
while packet is None:
    print(".", end="", flush=True)
    time.sleep(5)
    try:
        packet = device.check_data()
    except Exception as e:
        print("e", end="", flush=True)
print()

print(binascii.hexlify(packet))
