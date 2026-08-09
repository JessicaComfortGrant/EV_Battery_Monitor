import unittest
from unittest.mock import patch

from src.cli import get_float_input, display_result

class TestGetFloatInput(unittest.TestCase):
    
    @patch('builtins.input', return_value='400')
    def test_valid_input(self, mock_input):
        result = get_float_input("Enter battery voltage (V): ")
        self.assertEqual(result, 400.0)
        
    @patch('builtins.input', side_effect=['abc', '400'])
    @patch('builtins.print')
    def test_invalid_then_valid_input(self, mock_print, mock_input):
        result = get_float_input("Enter battery voltage (V): ")
        
        self.assertEqual(result, 400.0)
        mock_print.assert_called_once_with(
            "Invalid input. Please enter a number"
            )
        
    
    class TestDisplayResult(unittest.TestCase):
        
        @patch('builtins.print')
        def test_display_result(self, mock_print):
            result = {
                'voltage': 400.0,
                'current': 50.0,
                'power': 20.0,
                'temperature': 35.0,
                'temperature_status': 'NORMAL',
                'battery_status': 'NORMAL'
            }
            
            display_result(result)
            
            output = "\n".join(
                str(call.args[0]) for call in mock_print.call_args_list
            )
            
            self.assertIn("Voltage: 400.00 V", output)
            self.assertIn("Current: 50.00 A", output)
            self.assertIn("Power: 20.00 kW", output)
            self.assertIn("Temperature: 35.00 °C", output)
            self.assertIn("Temperature Status:  NORMAL", output)
            self.assertIn("Battery Status:      NORMAL", output)
        
        
        
        @patch("builtins.print")
        def test_display_warning_result(self, mock_print):
                result = {
                    "Voltage": 400,
                    "Current": 50,
                    "Temperature": 50,
                    "Power": 20.0,
                    "Temperature Status": "WARNING",
                    "Battery Status": "WARNING",
                }

                display_result(result)

                output = "\n".join(
                    str(call.args[0]) for call in mock_print.call_args_list
                )

                self.assertIn("WARNING", output)
                
                
            
        @patch("builtins.print")
        def test_display_critical_result(self, mock_print):
            result = {
                "Voltage": 400,
                "Current": 50,
                "Temperature": 65,
                "Power": 20.0,
                "Temperature Status": "CRITICAL",
                "Battery Status": "CRITICAL",
            }

            display_result(result)

            output = "\n".join(
                str(call.args[0]) for call in mock_print.call_args_list
            )

            self.assertIn("CRITICAL", output)


if __name__ == "__main__":
    unittest.main()

            
            