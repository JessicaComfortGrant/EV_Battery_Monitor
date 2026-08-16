import unittest

from src.battery_monitor import(
    Status, 
    monitor_battery
    ) 


class TestMonitorBatteryIntegration(unittest.TestCase):

    def test_healthy_battery_integration(self):
        result = monitor_battery(
            voltage=400,
            current=50,
            temperature=35,
            soc=50
        )

        self.assertEqual(result["voltage"], 400)
        self.assertEqual(result["current"], 50)
        self.assertEqual(result["temperature"], 35)
        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["soc_status"], Status.NORMAL)
        self.assertEqual(result["temperature_status"], Status.NORMAL)
        self.assertEqual(result["battery_status"], Status.NORMAL)

    def test_warning_battery_integration(self):
        result = monitor_battery(
            voltage=400,
            current=50,
            temperature=50,
            soc=50
        )

        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], Status.WARNING)
        self.assertEqual(result["battery_status"], Status.WARNING)
        self.assertEqual(result["soc_status"], Status.NORMAL)

    def test_critical_battery_integration(self):
        result = monitor_battery(
            voltage=400,
            current=50,
            temperature=65,
            soc=50
        )

        self.assertEqual(result["power"], 20.0)
        self.assertEqual(result["temperature_status"], Status.CRITICAL)
        self.assertEqual(result["battery_status"], Status.CRITICAL)
        self.assertEqual(result["soc_status"], Status.NORMAL)
      
        
    def test_low_voltage_integration(self):
        result = monitor_battery(
            voltage=299,
            current=50,
            temperature=35,
            soc=50
        )

        self.assertEqual(result["voltage_status"], Status.LOW)


    def test_normal_voltage_integration(self):
        result = monitor_battery(
            voltage=400,
            current=50,
            temperature=35,
            soc=50
        )

        self.assertEqual(result["voltage_status"], Status.NORMAL)


    def test_high_voltage_integration(self):
        result = monitor_battery(
            voltage=451,
            current=50,
            temperature=35,
            soc=50
        )

        self.assertEqual(result["voltage_status"], Status.HIGH)
        
    def test_low_current_integration(self):
        result = monitor_battery(
            voltage=400,
            current=24,
            temperature=35,
            soc=50
        )

        self.assertEqual(result["current_status"], Status.LOW)
    
    def test_normal_current_integration(self):
        result = monitor_battery(
            voltage=400,
            current=40,
            temperature=35,
            soc=50
        )

        self.assertEqual(result["current_status"], Status.NORMAL)
        self
        
    def test_high_current_integration(self):
        result = monitor_battery(
            voltage=400,
            current=51,
            temperature=35,
            soc=50
        )

        self.assertEqual(result["current_status"], Status.HIGH)
        self.assertEqual(result["soc_status"], Status.NORMAL)
        
        
    def test_low_soc_integration(self):
        result = monitor_battery(
            voltage=400,
            current=40,
            temperature=35,
            soc=10
        )

        self.assertEqual(result["soc_status"], Status.LOW)


    def test_normal_soc_integration(self):
        result = monitor_battery(
            voltage=400,
            current=40,
            temperature=35,
            soc=50
        )

        self.assertEqual(result["soc_status"], Status.NORMAL)


    def test_high_soc_integration(self):
        result = monitor_battery(
            voltage=400,
            current=40,
            temperature=35,
            soc=90
        )

        self.assertEqual(result["soc_status"], Status.HIGH)


if __name__ == "__main__":
    unittest.main()