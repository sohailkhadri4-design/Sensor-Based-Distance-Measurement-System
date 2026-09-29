from dataclasses import dataclass
from src.sensor.distance_processor import DistanceProcessor, ProcessedDistance
from src.sensor.hcsr04 import HCSR04Sensor, HCSR04TimeoutError

@dataclass
class DistanceMonitor:
    sensor: HCSR04Sensor
    processor: DistanceProcessor

    def sample(self) -> ProcessedDistance:
        try:
            raw = self.sensor.measure_distance_cm()
        except HCSR04TimeoutError:
            return ProcessedDistance(0.0, False, "TIMEOUT")
        return self.processor.process(raw)
