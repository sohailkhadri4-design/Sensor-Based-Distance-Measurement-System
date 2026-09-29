from src.application.distance_monitor import DistanceMonitor
from src.gpio.gpio_interface import SimulatedGPIO
from src.sensor.distance_processor import DistanceProcessor
from src.sensor.hcsr04 import HCSR04Pins, HCSR04Sensor

def test_monitor_processes_simulated_reading():
    gpio = SimulatedGPIO(echo_sequence=[False, True, True, False])
    monitor = DistanceMonitor(HCSR04Sensor(gpio, HCSR04Pins(23, 24)), DistanceProcessor())
    result = monitor.sample()
    assert result.valid and result.reason == "OK"
