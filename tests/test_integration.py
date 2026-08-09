import unittest

from src.battery_monitor import monitor_battery


class TestMonitorBatteryIntegration(unittest.TestCase):

    def test_healthy_battery_integration(self):
        result = monitor_battery(
            voltage=400,
            current=50,
            temperature=35
        )

        self.assertEqual(result["voltage"], 400)
        self.assertEqual(result["current"], 50)
        self.assertEqual(result["temperature"], 35)
        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], "NORMAL")
        self.assertEqual(result["battery_status"], "NORMAL")

    def test_warning_battery_integration(self):
        result = monitor_battery(
            voltage=400,
            current=50,
            temperature=50
        )

        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], "WARNING")
        self.assertEqual(result["battery_status"], "WARNING")

    def test_critical_battery_integration(self):
        result = monitor_battery(
            voltage=400,
            current=50,
            temperature=65
        )

        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], "CRITICAL")
        self.assertEqual(result["battery_status"], "CRITICAL")


if __name__ == "__main__":
    unittest.main()