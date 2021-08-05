import broadlink
import binascii

packet = b'2600920000012490183418101710183417341810181017101810171018101710181017101810171018101710181017101810173517341810171018101710181017341810173517101810173418101700028d1810171018101710181017101810171018341711171018101710181017101810171018101710181017101810171018101710181017101810173517341810171018000d05'
print(packet)

devices = broadlink.discover(timeout=5)
device = devices[0]
device.auth()

device.send_data(binascii.unhexlify(packet))