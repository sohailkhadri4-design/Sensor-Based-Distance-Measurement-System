from dataclasses import dataclass
from src.gpio.gpio_interface import GPIOInterface

class HCSR04TimeoutError(TimeoutError):
    pass

@dataclass(frozen=True)
class HCSR04Pins:
    trigger: int
    echo: int

class HCSR04Sensor:
    def __init__(self, gpio: GPIOInterface, pins: HCSR04Pins, echo_timeout_s: float = 0.03) -> None:
        if echo_timeout_s <= 0:
            raise ValueError("echo_timeout_s must be positive")
        self.gpio = gpio
        self.pins = pins
        self.echo_timeout_s = echo_timeout_s
        self.gpio.setup_output(pins.trigger)
        self.gpio.setup_input(pins.echo)
        self.gpio.write(pins.trigger, False)

    def measure_distance_cm(self) -> float:
        self._trigger()
        deadline = self.gpio.monotonic() + self.echo_timeout_s
        while not self.gpio.read(self.pins.echo):
            if self.gpio.monotonic() >= deadline:
                raise HCSR04TimeoutError("Echo did not go HIGH before timeout")
            self.gpio.wait(0.000001)

        start = self.gpio.monotonic()
        deadline = start + self.echo_timeout_s
        while self.gpio.read(self.pins.echo):
            if self.gpio.monotonic() >= deadline:
                raise HCSR04TimeoutError("Echo did not return LOW before timeout")
            self.gpio.wait(0.000001)

        return (self.gpio.monotonic() - start) * 34300.0 / 2.0

    def _trigger(self) -> None:
        self.gpio.write(self.pins.trigger, False)
        self.gpio.wait(0.000002)
        self.gpio.write(self.pins.trigger, True)
        self.gpio.wait(0.00001)
        self.gpio.write(self.pins.trigger, False)
