import bluetooth
import os
import jtalk
import ta7291
import time

while(True):
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    port = 1
    server_sock.bind(("", port))
    server_sock.listen(1)

    client_sock, address = server_sock.accept()
    print "Accepted connection from ", address

    speed = 8
    volume = 80

    d = ta7291.TA7291(18, 14, 15)

    while(True):
        try:
            data = client_sock.recv(1024)
        except bluetooth.btcommon.BluetoothError:
            break
        if data == 'm+':
            d.drive(100)
            time.sleep(0.35)
            d.brake()
            continue
        elif data == 'm-':
            d.drive(-100)
            time.sleep(0.35)
            d.brake()
            continue
        elif data == 's+':
            speed += 2
            speed = min([speed, 13])
            continue
        elif data == 's-':
            speed -= 2
            speed = max([speed, 3])
            continue
        print("received [%s]".format(data))
        print("speed is {}".format(speed))
        jtalk.jtalk(data, speed/10.0)

    client_sock.close()
    server_sock.close()
    d.cleanup()
