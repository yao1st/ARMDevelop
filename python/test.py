import serial
import time
import struct
s = serial.Serial('com3', 115200)

b = struct.pack('>ccc', b'a', b'\r', b'\n')

# b = struct.pack('>cHHcc',b'c',250,500,b'\r',b'\n')

print(b)
s.write(b)
s.close()