
import logging
import os

def get_logger(name):
        # Create logs directory if it doesn't exist
        os.makedirs("logs", exist_ok=True)
        
        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        
        # Avoid duplicate handlers
        if not logger.handlers:
            # File handler — writes to file
            file_handler = logging.FileHandler("logs/test_execution.log")
            file_handler.setLevel(logging.INFO)
            
            # Format
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger