

import serial

ports = serial.tools.list_ports.comports()


import serial
import serial.tools.list_ports

def is_port_open(port):
    try:
        ser = serial.Serial(port)
        ser.close()
        return False
    except serial.SerialException:
        return True

def list_and_check_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        port_name = port.device
        if is_port_open(port_name):
            print(f"{port_name} is occupied")
        else:
            print(f"{port_name} is available")

if __name__ == "__main__":
    list_and_check_ports()
    

