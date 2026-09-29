from collections import deque
from dataclasses import dataclass

@dataclass(frozen=True)
class ProcessedDistance:
    distance_cm: float
    valid: bool
    reason: str

class DistanceProcessor:
    def __init__(self, min_cm: float = 2.0, max_cm: float = 400.0, window_size: int = 3) -> None:
        if min_cm < 0 or max_cm <= min_cm:
            raise ValueError("Invalid distance range")
        if window_size < 1:
            raise ValueError("window_size must be at least 1")
        self.min_cm, self.max_cm = min_cm, max_cm
        self.window = deque(maxlen=window_size)

    def process(self, distance_cm: float) -> ProcessedDistance:
        if not self.min_cm <= distance_cm <= self.max_cm:
            return ProcessedDistance(distance_cm, False, "OUT_OF_RANGE")
        self.window.append(distance_cm)
        return ProcessedDistance(sum(self.window) / len(self.window), True, "OK")
