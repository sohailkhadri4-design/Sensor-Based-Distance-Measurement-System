# Measurement Processing

Distance is derived from echo pulse duration:

distance = time x speed_of_sound / 2

The implementation uses approximately 343 m/s for the speed of sound under room-temperature conditions.

Default validation range:
- Minimum: 2 cm
- Maximum: 400 cm

A configurable moving-average window reduces short-term measurement variation.

Timeouts are represented separately from out-of-range readings so application code can distinguish timing/communication problems from invalid measurements.
