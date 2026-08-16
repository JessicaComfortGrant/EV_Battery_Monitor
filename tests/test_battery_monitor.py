import unittest

from src.battery_monitor import (
    calculate_battery_power,
    evaluate_temperature,
    evaluate_voltage,
    evaluate_current,
    evaluate_soc,
    determine_battery_status,
    monitor_battery,
    Status
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
        self.assertEqual(evaluate_temperature(35), Status.NORMAL)
        
    def test_temperature_below_warning_threshold(self):
        self.assertEqual(evaluate_temperature(44.9), Status.NORMAL)
        
    def test_warning_at_lower_boundary(self):
        self.assertEqual(evaluate_temperature(45), Status.WARNING)
        
    def test_warning_at_upper_boundary(self):
        self.assertEqual(evaluate_temperature(60), Status.WARNING)
        
    def test_critical_above_threshold(self):
        self.assertEqual(evaluate_temperature(60.1), Status.CRITICAL)
        
    def test_high_temperature(self):
        self.assertEqual(evaluate_temperature(80), Status.CRITICAL)
        
        
class TestBatteryStatus(unittest.TestCase):
    def test_normal_status(self):
        self.assertEqual(
            determine_battery_status(
                Status.NORMAL,
                Status.NORMAL,
                Status.NORMAL,
                Status.NORMAL                 
            ),
            Status.NORMAL
        )
        
    def test_warning_status(self):
        self.assertEqual(
            determine_battery_status(
                Status.NORMAL,
                Status.NORMAL,
                Status.WARNING,
                Status.NORMAL
            ),
            Status.WARNING
        )
        
    def test_critical_status(self):
        self.assertEqual(
            determine_battery_status(
                Status.NORMAL,
                Status.NORMAL,
                Status.CRITICAL,
                Status.NORMAL
            ),
            Status.CRITICAL
        )
        
    def test_voltage_low_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                Status.LOW,
                Status.NORMAL,
                Status.NORMAL,
                Status.NORMAL
            ),
            Status.NORMAL
        )

    def test_voltage_high_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                Status.HIGH,
                Status.NORMAL,
                Status.NORMAL,
                Status.NORMAL
            ),
            Status.NORMAL
        )

    def test_current_low_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                Status.NORMAL,
                Status.LOW,
                Status.NORMAL,
                Status.NORMAL
            ),
            Status.NORMAL
        )

    def test_current_high_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                Status.NORMAL,
                Status.HIGH,
                Status.NORMAL,
                Status.NORMAL
            ),
            Status.NORMAL
        )

    def test_low_soc_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                Status.NORMAL,
                Status.NORMAL,
                Status.NORMAL,
                Status.LOW
            ),
            Status.NORMAL
        )

    def test_high_soc_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                Status.NORMAL,
                Status.NORMAL,
                Status.NORMAL,
                Status.HIGH
            ),
            Status.NORMAL
        )
    
    
    
        
                

class TestMonitorBattery(unittest.TestCase):
    def test_healthy_battery(self):
        result = monitor_battery(400, 50, 35, 50)
        
        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], Status.NORMAL)
        self.assertEqual(result["battery_status"], Status.NORMAL)
        
    
    def test_warm_battery(self):
        result = monitor_battery(400, 50, 50, 50)
        
        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], Status.WARNING)
        self.assertEqual(result["battery_status"], Status.WARNING)
        
    def test_overheated_battery(self):
        result = monitor_battery(400,50,65,50)
        
        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], Status.CRITICAL)
        self.assertEqual(result["battery_status"], Status.CRITICAL)
        

class TestEvaluateVoltage(unittest.TestCase):

    def test_low_voltage(self):
        self.assertEqual(evaluate_voltage(299), Status.LOW)

    def test_normal_voltage(self):
        self.assertEqual(evaluate_voltage(400), Status.NORMAL)

    def test_high_voltage(self):
        self.assertEqual(evaluate_voltage(451), Status.HIGH)

    def test_normal_at_lower_boundary(self):
        self.assertEqual(evaluate_voltage(300), Status.NORMAL)

    def test_normal_at_upper_boundary(self):
        self.assertEqual(evaluate_voltage(450), Status.NORMAL)
        

class TestEvaluateCurrent(unittest.TestCase):
    
    def test_low_current(self):
        self.assertEqual(evaluate_current(24.9), Status.LOW)
    
    def test_normal_at_lower_boundary(self):
            self.assertEqual(evaluate_current(25), Status.NORMAL)
        
    def test_normal_current(self):
        self.assertEqual(evaluate_current(40), Status.NORMAL)
    
    def test_normal_at_upper_boundary(self):
            self.assertEqual(evaluate_current(50), Status.NORMAL)
   
    def test_high_current(self):
        self.assertEqual(evaluate_current(50.1), Status.HIGH)
        

class TestEvaluateSOC(unittest.TestCase):
    
    def test_low_soc(self):
        self.assertEqual(evaluate_soc(19.9), Status.LOW)
        
    def test_normal_at_lower_boundary(self):
        self.assertEqual(evaluate_soc(20), Status.NORMAL)
        
    def test_normal_soc(self):
        self.assertEqual(evaluate_soc(50), Status.NORMAL)
        
    def test_normal_at_upper_boundary(self):
        self.assertEqual(evaluate_soc(80), Status.NORMAL)
        
    def test_high_soc(self):
        self.assertEqual(evaluate_soc(80.1), Status.HIGH)


if __name__ == "__main__":
    unittest.main()