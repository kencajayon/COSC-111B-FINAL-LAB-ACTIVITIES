from fastapi import FastAPI
import serial
import time
import threading
import sys
import os  

PORT = 'COM4' 
BAUD = 9600


def show_instructions():
    
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass
    print("=" * 55)
    print(" LAB 6: BIDIRECTIONAL USING PYTHON AND ARDUINO ".center(55, "#"))
    print("-" * 55)


def listen_to_arduino(ser):
    while ser.is_open:
        if ser.in_waiting > 0:
            try:
                btn_signal = ser.readline().decode('utf-8').strip().upper()
                if btn_signal == 'R':
                    ser.write(b'1')
                    print("Physical Button: RED Toggle")
                elif btn_signal == 'G':
                    ser.write(b'2')
                    print("Physical Button: GREEN Toggle")
                elif btn_signal == 'B':
                    ser.write(b'3')
                    print("Physical Button: BLUE Toggle")
            except:
                pass
        time.sleep(0.01)


arduino = None


try:
    arduino = serial.Serial(PORT, BAUD, timeout=0.1)
    time.sleep(2)
    show_instructions()

    listener_thread = threading.Thread(target=listen_to_arduino, args=(arduino,), daemon=True)
    listener_thread.start()
    
except Exception as e:
    print(f"\n[!] Error connecting to Arduino: {e}")



app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Arduino API is running"}

@app.get("/led/{color}")
def toggle_led(color: str):
    if arduino is None or not arduino.is_open:
        return {"error": "Arduino not connected"}

    color = color.lower()
    
    if color == "red":
        arduino.write(b'1')
        return {"message": "Red LED Toggled"}
    
    elif color == "green":
        arduino.write(b'2')
        return {"message": "Green LED Toggled"}
    
    elif color == "blue":
        arduino.write(b'3')
        return {"message": "Blue LED Toggled"}
    
    else:
        return {"error": "Invalid color. Use red, green, or blue."}

@app.get("/led/on")
def turn_all_on():
    if arduino is None or not arduino.is_open:
        return {"error": "Arduino not connected"}
        
    arduino.write(b'1')
    time.sleep(0.1)
    arduino.write(b'2')
    time.sleep(0.1)
    arduino.write(b'3')
    return {"message": "Toggled ALL LEDs"}

@app.get("/led/off")
def turn_all_off():
    if arduino is None or not arduino.is_open:
        return {"error": "Arduino not connected"}

    arduino.write(b'1')
    time.sleep(0.1)
    arduino.write(b'2')
    time.sleep(0.1)
    arduino.write(b'3')
    return {"message": "Toggled ALL LEDs"}