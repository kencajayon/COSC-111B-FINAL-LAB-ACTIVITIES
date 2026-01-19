import serial
import requests
import time


# --- Configuration ---
SERIAL_PORT = 'COM4'  # Update this (e.g., '/dev/ttyUSB0' on Linux/Mac)
BAUD_RATE = 9600
BASE_URL = "http://172.20.10.3:8000"



 # Replace with provided URL

def start_client():
    try:
        # Initialize Serial Connection
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"--- Listening for Arduino on {SERIAL_PORT} ---")
        
        while True:
            if ser.in_waiting > 0:
                # Read and normalize input
                raw_data = ser.readline().decode('utf-8').strip()
                
                if raw_data:
                    # Logic: Extract number, normalize to lowercase
                    normalized_data = raw_data.lower() # e.g., "group_1"
                    
                    try:
                        # Extract number (assuming format "group_x")
                        group_num = normalized_data.split('_')[1]
                        endpoint = f"{BASE_URL}/led/group/4/toggle"
                        
                        print(f"\n[EVENT] Received: {raw_data}")
                        print(f"[ACTION] Calling: {endpoint}")
                        
                        # Send HTTP Request
                        response = requests.get(endpoint)
                        
                        if response.status_code == 200:
                            print(f"[SUCCESS] API Response: {response.status_code} OK")
                        else:
                            print(f"[ERROR] API Response: {response.status_code}")
                            
                    except (IndexError, ValueError):
                        print(f"[VALIDATION ERROR] Invalid serial format: {raw_data}")
                    except requests.exceptions.RequestException as e:
                        print(f"[CONNECTION ERROR] Could not reach API: {e}")

            time.sleep(0.1) # Prevent CPU hogging

    except serial.SerialException:
        print("Error: Could not open serial port. Is the Arduino connected?")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    start_client()
