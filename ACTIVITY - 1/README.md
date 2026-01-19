- Description of the Activity 

  In this laboratory activity, we worked with digital signals using Arduino.
The goal of this activity is to create a running light circuit using LEDs.
This activity helps us understand how digital output pins work and how digitalWrite() is used to control electronic components.

- Circuit Setup 

  The LEDs are connected to digital pins 8 to 12 of the Arduino.
Each LED is connected in series with a resistor and all grounds are connected to the GND pin of the Arduino.

  ( A breadboard diagram is included in this folder. )

- Code Explanation 

  First, pins 8 to 12 are set as OUTPUT using the pinMode() function.
In the loop() function, the LEDs turn ON one by one starting from pin 12 to pin 8 with a 1-second delay.
After all LEDs are ON, they turn OFF one by one in the same order.

- The function digitalWrite(HIGH) is used to turn ON the LEDs and digitalWrite(LOW) is used to turn them OFF.

