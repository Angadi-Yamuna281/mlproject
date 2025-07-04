import logging
import os
from datetime import datetime

# Step 1: Create a folder called 'logs' if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Step 2: Create log file name with timestamp
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Step 3: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Step 4: Create a logger object to use elsewhere
if __name__ == "__main__":
    logging.info("Logger initialized successfully.")
    print(f"Log file created at: {LOG_FILE_PATH}")