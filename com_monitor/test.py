
import serial
import serial.tools
import serial.tools.list_ports
import threading

ports = serial.tools.list_ports.comports()
for port in ports:
    print(port)

def read_from_com_port(source_port, dest_port, baudrate=9600, timeout=1):
    try:
        ser_source = serial.Serial(source_port, baudrate, timeout=timeout)
        ser_dest = serial.Serial(dest_port, baudrate, timeout=timeout)
        print(f"Forwarding data from {source_port} to {dest_port}...")
        
        while True:
            data = ser_source.readline()
            if data:
                ser_dest.write(data)
                print(f"Forwarded: {data.decode('utf-8').strip()}")
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        ser_source.close()
        ser_dest.close()
        print("Program interrupted")

def main():
    source_port = 'COM1'  # 原始端口
    dest_port = 'COM2'    # 虚拟端口
    
    read_thread = threading.Thread(target=read_from_com_port, args=(source_port, dest_port))
    read_thread.start()

if __name__ == "__main__":
    main()
