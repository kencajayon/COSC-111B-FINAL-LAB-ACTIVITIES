- Description of the Activity

  In this final laboratory activity, we designed and implemented an Arduino-to-Python client system that uses serial communication and an HTTP-based API.

  The Arduino uses a push button as an input device. Instead of directly controlling LEDs or making HTTP requests, the Arduino sends a signal to a Python client program through the Serial connection. The Python program then calls a predefined API endpoint to remotely control an LED system.

  This activity demonstrates proper separation of responsibilities between Arduino hardware control and software-based API communication.

- Arduino Program Logic

  A push button is connected to the Arduino as an input device

  Software debouncing is implemented to ensure:

  - One button press = one signal

  When a valid button press is detected:

  - Arduino sends only one serial signal

  - The signal represents the assigned group number

  The Arduino:

  - Does NOT make HTTP requests

  - Does NOT control any LEDs

- Python Client Program Logic

  The Python program runs as a non-terminating application

  It continuously listens to the serial port connected to Arduino

  When a valid serial input is received:

  - The group number is extracted

  - Input is normalized to avoid case-sensitivity issues

  An HTTP request is sent to the API endpoint using the format:

  - /led/group/<number>/toggle

  - The base API URL is provided by the instructor

  The Python program displays the following in the terminal:

  - Group number received

  - API endpoint called

  - API response (success or error)

- Communication and Behavior Rules

  - One button press results in one API request

  - Long button presses do NOT generate repeated API calls

  - All serial inputs are validated

  - Proper error messages are displayed when invalid input is detected
