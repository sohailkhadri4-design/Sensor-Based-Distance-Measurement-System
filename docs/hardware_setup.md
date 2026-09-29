# Hardware Setup

The HC-SR04 typically provides VCC, TRIG, ECHO, and GND.

Use the exact wiring and electrical interface recommended by the sensor documentation and the Raspberry Pi board documentation.

Important: on common 5 V HC-SR04 configurations, the ECHO signal may exceed Raspberry Pi GPIO voltage tolerance. Use an appropriate level-shifting or voltage-divider circuit before connecting ECHO.

The repository intentionally does not prescribe a personal hardware pinout. Configure HCSR04Pins to match the actual wiring.

Bring-up checklist:
1. Confirm common ground.
2. Confirm sensor supply voltage.
3. Verify TRIG wiring.
4. Protect/level-shift ECHO as required.
5. Confirm GPIO numbering mode.
6. Use a conservative timeout.
7. Compare readings against known distances.
