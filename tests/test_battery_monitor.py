import unittest

from src.battery_monitor import (
    calculate_battery_power,
    evaluate_temperature,
    determine_battery_status,
    monitor_battery,
    NORMAL,
    WARNING,
    CRITICAL,
)

class TestCalculatePower(unittest.TestCase):
    def test_normal_power(self):
        self.assertEqual(calculate_battery_power(400, 50), 20.0)
        
    def test_lower_power(self):
        self.assertEqual(calculate_battery_power(350, 20), 7.0)
        
    def test_zero_power(self):
        self.assertEqual(calculate_battery_power(400, 0), 0.0)
        
        
class TestEvaluateTemperature(unittest.TestCase):
    def test_normal_temperature(self):
        self.assertEqual(evaluate_temperature(35), NORMAL)
        
    def test_temperature_below_warning_threshold(self):
        self.assertEqual(evaluate_temperature(44.9), NORMAL)
        
    def test_warning_at_lower_boundary(self):
        self.assertEqual(evaluate_temperature(45), WARNING)
        
    def test_warning_at_upper_boundary(self):
        self.assertEqual(evaluate_temperature(60), WARNING)
        
    def test_critical_above_threshold(self):
        self.assertEqual(evaluate_temperature(60.1), CRITICAL)
        
    def test_high_temperature(self):
        self.assertEqual(evaluate_temperature(80), CRITICAL)
        
        
class TestBatteryStatus(unittest.TestCase):
    def test_normal_status(self):
        self.assertEqual(determine_battery_status(NORMAL), NORMAL)
        
    def test_warning_status(self):
        self.assertEqual(determine_battery_status(WARNING), WARNING)
        
    def test_critical_status(self):
        self.assertEqual(determine_battery_status(CRITICAL), CRITICAL)


class TestMonitorBattery(unittest.TestCase):
    def test_healthy_battery(self):
        result = monitor_battery(400, 50, 35)
        
        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], NORMAL)
        self.assertEqual(result["battery_status"], NORMAL)
        
    
    def test_warm_battery(self):
        result = monitor_battery(400, 50, 50)
        
        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], WARNING)
        self.assertEqual(result["battery_status"], WARNING)
        
        
    def test_overheated_battery(self):
        result = monitor_battery(400,50,65)
        
        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], CRITICAL)
        self.assertEqual(result["battery_status"], CRITICAL)


if __name__ == "__main__":
    unittest.main()