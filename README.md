# Sensor-Based Distance Measurement System

Real-time ultrasonic distance measurement using Raspberry Pi, Python, GPIO, and an HC-SR04 sensor.

## Overview
This project demonstrates a structured sensor-processing application for measuring distance with an HC-SR04 ultrasonic sensor. GPIO access, sensor timing, measurement validation, filtering, and application logic are separated so the core behavior can be tested without Raspberry Pi hardware.

## Features
- HC-SR04 trigger/echo timing
- Distance calculation in centimeters
- Configurable measurement timeout
- Invalid and out-of-range reading handling
- Moving-average filtering
- Raspberry Pi GPIO adapter with simulated GPIO backend
- Unit and integration tests
- GitHub Actions CI
- Hardware setup and troubleshooting documentation

> Hardware note: this repository contains testable reference code and a Raspberry Pi GPIO adapter. It does not claim a particular physical wiring configuration or measured hardware results unless those are documented separately.

## Architecture
HC-SR04 -> GPIO Interface -> HCSR04 Sensor -> Distance Processor -> Distance Monitor

## Repository structure
- src/application/distance_monitor.py
- src/gpio/gpio_interface.py
- src/sensor/hcsr04.py
- src/sensor/distance_processor.py
- tests/
- examples/run_distance_monitor.py
- docs/

## Distance calculation
distance_cm = echo_time_seconds * 34300 / 2

A configurable timeout prevents a missing echo from blocking the application indefinitely.

## Run
Requires Python 3.9+.

    python -m pip install -r requirements.txt
    python -m pytest -q

The tests use simulated GPIO, so Raspberry Pi hardware is not required for CI.

Run the example:

    python examples/run_distance_monitor.py

## Raspberry Pi integration
Install the GPIO library appropriate for the Raspberry Pi OS/Python environment, then configure HCSR04Pins for the actual wiring.

The example pin values are placeholders. Verify voltage levels, wiring, grounding, and the sensor datasheet before connecting hardware.

## Troubleshooting
The documentation covers echo timeout, GPIO configuration, trigger timing, grounding, invalid readings, and out-of-range measurements.

## Scope
This project focuses on ultrasonic distance measurement and sensor-processing logic. It does not claim autonomous navigation, obstacle avoidance, localization, or physical test results unless those are added and documented.

## Author
Syed Sohel Khadri
Embedded Firmware | STM32 | ARM Cortex-M | Embedded C
