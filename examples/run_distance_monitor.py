from src.application.distance_monitor import DistanceMonitor
from src.gpio.gpio_interface import SimulatedGPIO
from src.sensor.distance_processor import DistanceProcessor
from src.sensor.hcsr04 import HCSR04Pins, HCSR04Sensor

gpio = SimulatedGPIO(echo_sequence=[False, True, True, False])
sensor = HCSR04Sensor(gpio, HCSR04Pins(trigger=23, echo=24))
result = DistanceMonitor(sensor, DistanceProcessor()).sample()
print(f"Distance: {result.distance_cm:.2f} cm | status={result.reason}")
