import serial
import time
import threading

serialInstance = serial.Serial("COM1", 9600, timeout=1)
time.sleep(2)

def send(message):
   serialInstance.write((message + '\n').encode("utf-8"))
   print(f"sent {message}")

def receive():
   if serialInstance.in_waiting > 0:
       data = serialInstance.readline().decode("utf-8").strip()
       if data:
           print(f"received {data}")
           return data
   return None

def received_continuously():
   while True:
       received_data = receive()
       time.sleep(0.1)

received_thread_instance = threading.Thread(target=received_continuously, daemon=True)
received_thread_instance.start()

try:
   while True:
       message = input("Enter message: ")
       if message:
           send(message)
except KeyboardInterrupt:
   print("Exiting...")
finally:
   serialInstance.close()

