# System Architecture

The system is divided into four layers:

1. GPIO interface: isolates hardware-specific GPIO operations.
2. HC-SR04 driver: generates the trigger pulse, waits for echo transitions, applies a timeout, and converts echo duration to distance.
3. Distance processor: validates readings and applies a moving-average filter.
4. Distance monitor: coordinates sampling and represents timeout as a structured status.

This separation keeps hardware access independent from processing logic and allows automated tests with simulated GPIO.
