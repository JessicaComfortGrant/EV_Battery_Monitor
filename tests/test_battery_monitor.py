import unittest

from src.battery_monitor import (
    calculate_battery_power,
    evaluate_temperature,
    evaluate_voltage,
    evaluate_current,
    evaluate_soc,
    determine_battery_status,
    monitor_battery,
    LOW,
    HIGH,
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
        self.assertEqual(
            determine_battery_status(
                NORMAL,
                NORMAL,
                NORMAL,
                NORMAL                 
            ),
            NORMAL
        )
        
    def test_warning_status(self):
        self.assertEqual(
            determine_battery_status(
                NORMAL,
                NORMAL,
                WARNING,
                NORMAL
            ),
            WARNING
        )
        
    def test_critical_status(self):
        self.assertEqual(
            determine_battery_status(
                NORMAL,
                NORMAL,
                CRITICAL,
                NORMAL
            ),
            CRITICAL
        )
        
    def test_voltage_low_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                LOW,
                NORMAL,
                NORMAL,
                NORMAL
            ),
            NORMAL
        )

    def test_voltage_high_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                HIGH,
                NORMAL,
                NORMAL,
                NORMAL
            ),
            NORMAL
        )

    def test_current_low_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                NORMAL,
                LOW,
                NORMAL,
                NORMAL
            ),
            NORMAL
        )

    def test_current_high_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                NORMAL,
                HIGH,
                NORMAL,
                NORMAL
            ),
            NORMAL
        )

    def test_low_soc_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                NORMAL,
                NORMAL,
                NORMAL,
                LOW
            ),
            NORMAL
        )

    def test_high_soc_is_health_indicator(self):
        self.assertEqual(
            determine_battery_status(
                NORMAL,
                NORMAL,
                NORMAL,
                HIGH
            ),
            NORMAL
        )
    
    
    
        
                

class TestMonitorBattery(unittest.TestCase):
    def test_healthy_battery(self):
        result = monitor_battery(400, 50, 35, 50)
        
        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], NORMAL)
        self.assertEqual(result["battery_status"], NORMAL)
        
    
    def test_warm_battery(self):
        result = monitor_battery(400, 50, 50, 50)
        
        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], WARNING)
        self.assertEqual(result["battery_status"], WARNING)
        
        
    def test_overheated_battery(self):
        result = monitor_battery(400,50,65,50)
        
        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], CRITICAL)
        self.assertEqual(result["battery_status"], CRITICAL)
        

class TestEvaluateVoltage(unittest.TestCase):

    def test_low_voltage(self):
        self.assertEqual(evaluate_voltage(299), LOW)

    def test_normal_voltage(self):
        self.assertEqual(evaluate_voltage(400), NORMAL)

    def test_high_voltage(self):
        self.assertEqual(evaluate_voltage(451), HIGH)

    def test_normal_at_lower_boundary(self):
        self.assertEqual(evaluate_voltage(300), NORMAL)

    def test_normal_at_upper_boundary(self):
        self.assertEqual(evaluate_voltage(450), NORMAL)
        

class TestEvaluateCurrent(unittest.TestCase):
    
    def test_low_current(self):
        self.assertEqual(evaluate_current(24.9), LOW)
    
    def test_normal_at_lower_boundary(self):
            self.assertEqual(evaluate_current(25), NORMAL)
        
    def test_normal_current(self):
        self.assertEqual(evaluate_current(40), NORMAL)
    
    def test_normal_at_upper_boundary(self):
            self.assertEqual(evaluate_current(50), NORMAL)
   
    def test_high_current(self):
        self.assertEqual(evaluate_current(50.1), HIGH)
        

class TestEvaluateSOC(unittest.TestCase):
    
    def test_low_soc(self):
        self.assertEqual(evaluate_soc(19.9), LOW)
        
    def test_normal_at_lower_boundary(self):
        self.assertEqual(evaluate_soc(20), NORMAL)
        
    def test_normal_soc(self):
        self.assertEqual(evaluate_soc(50), NORMAL)
        
    def test_normal_at_upper_boundary(self):
        self.assertEqual(evaluate_soc(80), NORMAL)
        
    def test_high_soc(self):
        self.assertEqual(evaluate_soc(80.1), HIGH)


if __name__ == "__main__":
    unittest.main()