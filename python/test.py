import serial

s = serial.Serial('com3', 115200)
# s.open()
s.write(b'ok\r\n')
# print(str(s.readline(), encoding = "utf-8"))
s.close()