- Description of the Activity

  In this laboratory activity, we implemented bidirectional serial communication between Arduino and Python.
The system allows Arduino to send data to Python (outbound) and Python to send commands back to Arduino (inbound).

  Push buttons are used to send signals from Arduino to Python, while Python sends commands to Arduino to control LEDs.

- Circuit Setup

  LEDs

  - Red LED - Digital pin 7

  - Green LED - Digital pin 6

  - Blue LED - Digital pin 5

  Push Buttons

  - Button 1 - Digital pin 12

  - Button 2 - Digital pin 11

  - Button 3 - Digital pin 10

All components share a common GND.

A breadboard diagram is included in this folder.

- Program Logic and Code Explanation

  Outbound Signal (Arduino → Python)

  - When Button 1 is pressed, Arduino sends "R" once

  - When Button 2 is pressed, Arduino sends "G" once

  - When Button 3 is pressed, Arduino sends "B" once

  - No LED action happens when buttons are pressed

  - Only the transmitted signal is shown in Python

  Inbound Signal (Python → Arduino)

  - When Python sends "1", the Red LED toggles ON/OFF

  - When Python sends "2", the Green LED toggles ON/OFF

  - When Python sends "3", the Blue LED toggles ON/OFF

All inputs are case-insensitive

- Python Side Logic

  Python continuously listens for input from Arduino

  When:

  - "R" is received - Python sends back "1"

  - "G" is received - Python sends back "2"

  - "B" is received - Python sends back "3"

Response time is less than 1 second
