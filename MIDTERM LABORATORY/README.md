- Description of the Activity

  In this midterm laboratory exam, we designed and programmed a smart lighting system using Arduino.
The system uses a photoresistor (LDR) to measure light intensity and automatically adjusts LED indicators based on environmental lighting conditions.

  The system supports two modes:

  - Manual Mode, where the user sets threshold values through the Serial Monitor

  - Automatic Mode, where thresholds are adjusted automatically based on simulated environmental conditions

- Circuit Setup

  The photoresistor is connected to an analog pin to measure light intensity

  Three LEDs are used as indicators:

  - Green LED – Low light intensity

  - Yellow LED – Medium light intensity

  - Red LED – High light intensity

  Only one LED is active at a time

  All components share a common GND

   ( A breadboard diagram is included in this folder.)

- System Logic and LED Behavior

  Light Intensity Levels

  The sensor value is converted from 0–1023 to 0–100%.

  - Low Intensity - Green LED ON

  - Medium Intensity - Yellow LED ON

  - High Intensity - Red LED ON

- Automatic Mode Behavior

  In automatic mode, threshold values are adjusted automatically based on simulated environmental conditions:

  Cloudy:

  - Low: 0%

  - High: 40%

  Normal / Clear:

  - Low: 41%

  - High: 70%

  Bright Sunlight:

  - Low: 71%

  - High: 100%
 
  
