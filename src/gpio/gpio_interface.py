from dataclasses import dataclass
from typing import Protocol

class GPIOInterface(Protocol):
    def setup_output(self, pin: int) -> None: ...
    def setup_input(self, pin: int) -> None: ...
    def write(self, pin: int, value: bool) -> None: ...
    def read(self, pin: int) -> bool: ...
    def wait(self, seconds: float) -> None: ...
    def monotonic(self) -> float: ...

@dataclass
class SimulatedGPIO:
    echo_sequence: list[bool]
    now: float = 0.0

    def setup_output(self, pin: int) -> None: pass
    def setup_input(self, pin: int) -> None: pass
    def write(self, pin: int, value: bool) -> None: pass

    def read(self, pin: int) -> bool:
        return self.echo_sequence.pop(0) if self.echo_sequence else False

    def wait(self, seconds: float) -> None:
        self.now += seconds

    def monotonic(self) -> float:
        return self.now

class RaspberryPiGPIO:
    """RPi.GPIO adapter; import is delayed so CI can run off Raspberry Pi."""

    def __init__(self, mode: int | None = None) -> None:
        import RPi.GPIO as GPIO
        self.GPIO = GPIO
        self.GPIO.setmode(mode if mode is not None else self.GPIO.BCM)

    def setup_output(self, pin: int) -> None:
        self.GPIO.setup(pin, self.GPIO.OUT, initial=self.GPIO.LOW)

    def setup_input(self, pin: int) -> None:
        self.GPIO.setup(pin, self.GPIO.IN)

    def write(self, pin: int, value: bool) -> None:
        self.GPIO.output(pin, self.GPIO.HIGH if value else self.GPIO.LOW)

    def read(self, pin: int) -> bool:
        return bool(self.GPIO.input(pin))

    def wait(self, seconds: float) -> None:
        import time
        time.sleep(seconds)

    def monotonic(self) -> float:
        import time
        return time.monotonic()
