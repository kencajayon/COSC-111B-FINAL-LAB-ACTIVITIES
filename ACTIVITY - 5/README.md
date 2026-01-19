- Description of the Activity

  In this laboratory activity, we implemented serial communication between Arduino and Python.
The goal of this activity is to control multiple LEDs connected to an Arduino board using serial input from a Python program.

  The system allows the user to send commands from Python to Arduino to turn LEDs ON and OFF.

- Circuit Setup

  - Red LED is connected to digital pin 8

  - Green LED is connected to digital pin 9

  - Blue LED is connected to digital pin 10

  - All LEDs share a common GND

  ( A breadboard diagram is included in this folder. )

- Program Logic and Code Explanation

  Arduino Side

  The Arduino sketch listens for serial input and performs the following actions:

  - R/r - Toggle Red LED ON or OFF

  - G/g - Toggle Green LED ON or OFF

  - B/b - Toggle Blue LED ON or OFF

  - A/a - Turn ALL LEDs ON

  - O/o - Turn ALL LEDs OFF

Any other input returns an error message

All inputs are case-insensitive.

- A Python script is used to send commands to the Arduino through the serial port.

  The program displays the following menu:

  - [R] Red ON/OFF
  - [G] Green ON/OFF
  - [B] Blue ON/OFF
  - [A] All ON
  - [O] All OFF
  - [X] Exit


The script runs continuously (non-terminating loop)

When X/x is entered, the Python program terminates

All inputs are case-insensitive

