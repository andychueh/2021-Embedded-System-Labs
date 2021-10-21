import socket
import numpy as np 
import json
import matplotlib.pyplot as plt;
HOST = "192.168.0.156"
PORT = 3050
# Standard loopback interface address
# Port to listen on (use ports > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print('Received from socket server:',data)
            try:
                obj = json.loads(data)
            except:
                continue
            plt.ion()
            plt.subplot(131)
            plt.scatter(obj["s"], obj["acc_x"], c="red")
            plt.scatter(obj["s"], obj["acc_y"], c="green")
            plt.scatter(obj["s"], obj["acc_z"], c="blue")
            plt.xlabel("Number of Sampling")
            plt.ylabel("Acceleration (m/s) Red: X Green: Y Blue: Z")
            plt.subplot(132)
            plt.scatter(obj["s"], obj["pressure"], c="purple")
            plt.xlabel("Number of Sampling")
            plt.ylabel("Pressure (hPa)")
            plt.subplot(133)
            plt.scatter(obj["s"], obj["humidity"], c="orange")
            plt.xlabel("Number of Sampling")
            plt.ylabel("Relative Humidity (%Percentage)")
            plt.pause(0.5)
