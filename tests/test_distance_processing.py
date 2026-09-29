from src.sensor.distance_processor import DistanceProcessor

def test_valid_reading_is_processed():
    result = DistanceProcessor(window_size=3).process(100.0)
    assert result.valid and result.distance_cm == 100.0 and result.reason == "OK"

def test_out_of_range_reading_is_rejected():
    result = DistanceProcessor().process(500.0)
    assert not result.valid and result.reason == "OUT_OF_RANGE"

def test_moving_average_is_applied():
    processor = DistanceProcessor(window_size=3)
    processor.process(100.0)
    processor.process(110.0)
    assert processor.process(120.0).distance_cm == 110.0
