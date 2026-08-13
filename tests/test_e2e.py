import unittest
from unittest.mock import patch

from src.cli import main


class TestBatteryMonitorE2E(unittest.TestCase):

    @patch("builtins.input", side_effect=[
        "400",
        "50",
        "35",
        "50"
    ])
    @patch("builtins.print")
    
    def test_healthy_battery_e2e(self, mock_print, mock_input):
        main()
        output = "\n".join(
            str(call.args[0])
            for call in mock_print.call_args_list
            if call.args
        )

        self.assertIn("Voltage:             400.00 V", output)
        self.assertIn("Current:             50.00 A", output)
        self.assertIn("Power:               20.00 kW", output)
        self.assertIn("Temperature:         35.00 °C", output)
        self.assertIn("State of Charge:     50.00 %", output)

        self.assertIn("Voltage Status:      NORMAL", output)
        self.assertIn("Current Status:      NORMAL", output)
        self.assertIn("Temperature Status:  NORMAL", output)
        self.assertIn("SOC Status:          NORMAL", output)
        self.assertIn("Battery Status:      NORMAL", output)



    @patch("builtins.input", side_effect=[
    "400",
    "50",
    "50",
    "50"
    ])
    @patch("builtins.print")
    def test_warning_battery_e2e(self, mock_print, mock_input):
        main()

        output = "\n".join(
            str(call.args[0])
            for call in mock_print.call_args_list
            if call.args
        )

        self.assertIn("Voltage:             400.00 V", output)
        self.assertIn("Current:             50.00 A", output)
        self.assertIn("Power:               20.00 kW", output)
        self.assertIn("Temperature:         50.00 °C", output)
        self.assertIn("State of Charge:     50.00 %", output)

        self.assertIn("Voltage Status:      NORMAL", output)
        self.assertIn("Current Status:      NORMAL", output)
        self.assertIn("Temperature Status:  WARNING", output)
        self.assertIn("SOC Status:          NORMAL", output)
        self.assertIn("Battery Status:      WARNING", output)
    
        
    @patch("builtins.input", side_effect=[
    "400",
    "50",
    "65",
    "50"
    ])
    @patch("builtins.print")
    def test_critical_battery_e2e(self, mock_print, mock_input):
        main()

        output = "\n".join(
            str(call.args[0])
            for call in mock_print.call_args_list
            if call.args
        )

        self.assertIn("Voltage:             400.00 V", output)
        self.assertIn("Current:             50.00 A", output)
        self.assertIn("Power:               20.00 kW", output)
        self.assertIn("Temperature:         65.00 °C", output)
        self.assertIn("State of Charge:     50.00 %", output)

        self.assertIn("Voltage Status:      NORMAL", output)
        self.assertIn("Current Status:      NORMAL", output)
        self.assertIn("Temperature Status:  CRITICAL", output)
        self.assertIn("SOC Status:          NORMAL", output)
        self.assertIn("Battery Status:      CRITICAL", output)
    

if __name__ == "__main__":
    unittest.main()