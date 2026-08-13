import logging

def setup_logger():
    
    """Configure and return the battery monitor logger."""
    
    logger = logging.getLogger("battery_monitor")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        
        file_handler = logging.FileHandler("battery_monitor.log")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    return logger