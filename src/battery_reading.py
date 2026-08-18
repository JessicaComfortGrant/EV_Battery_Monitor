from dataclasses import dataclass

@dataclass
class BatteryReading:
    voltage: float
    current: float
    temperature: float
    soc: float
    timestamp: str