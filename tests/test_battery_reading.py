import unittest

from src.battery_reading import BatteryReading

class TestBatteryReading(unittest.TestCase):
    def test_battery_reading_initialization(self):
        reading = BatteryReading(
            voltage=400.0,
            current=50.0,
            temperature=35.0,
            soc=50.0,
            timestamp="2026-08-18 21:00:00"
        )

        self.assertEqual(reading.voltage, 400.0)
        self.assertEqual(reading.current, 50.0)
        self.assertEqual(reading.temperature, 35.0)
        self.assertEqual(reading.soc, 50.0)
        self.assertEqual(reading.timestamp, "2026-08-18 21:00:00")
        
if __name__ == "__main__":
    unittest.main()