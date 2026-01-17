- Description of the Activity

  In this laboratory activity, we worked with Arduino Serial Connection to control a circuit using the Serial Monitor.
A sensor-based system is implemented where the LED behavior can be controlled through serial input commands.

  The LED will blink when the sensor threshold is reached and will continue blinking until the word "stop" is entered in the Serial Monitor.

- Circuit Setup

  Only one sensor is used in this activity:

  - Thermistor (temperature threshold: 50°C), or
  -  Photoresistor (brightness threshold: 220)

   The LED is connected to digital pin 8 and all components share a common GND.

   ( The same circuit diagram from Laboratory Activity 3 is used. )
  

- Program Logic and Code Explanation

  The program continuously reads the sensor value.
When the sensor reaches the set threshold, the LED starts blinking with a delay of 100 ms.
Once blinking starts, it continues blinking even if the sensor value goes below the threshold.
  
- The Serial Monitor is used to control the LED:

  - When the word "stop" is entered (case-insensitive), the LED blinking stops.
  -  Serial input is handled using Arduino Serial functions.
