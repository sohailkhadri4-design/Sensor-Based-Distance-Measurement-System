from src.gpio.gpio_interface import SimulatedGPIO
from src.sensor.hcsr04 import HCSR04Pins, HCSR04Sensor, HCSR04TimeoutError

def test_sensor_timeout_when_echo_never_arrives():
    gpio = SimulatedGPIO(echo_sequence=[False] * 1000)
    sensor = HCSR04Sensor(gpio, HCSR04Pins(23, 24), echo_timeout_s=0.00001)
    try:
        sensor.measure_distance_cm()
    except HCSR04TimeoutError:
        return
    assert False, "Expected HCSR04TimeoutError"

def test_sensor_detects_echo_sequence():
    gpio = SimulatedGPIO(echo_sequence=[False, True, True, False])
    distance = HCSR04Sensor(gpio, HCSR04Pins(23, 24)).measure_distance_cm()
    assert distance > 0
