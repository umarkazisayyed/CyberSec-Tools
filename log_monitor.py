import time

# Path to the log file (Change this to the actual log file you want to monitor)
LOG_FILE_PATH = "security.log"

# Suspicious patterns to detect
SUSPICIOUS_PATTERNS = [
    "failed password",
    "unauthorized access",
    "brute force",
    "malicious IP",
    "denied",
]

def monitor_log():
    try:
        with open(LOG_FILE_PATH, "r") as file:
            file.seek(0, 2)  # Move to the end of the file
            print(f"🔍 Monitoring {LOG_FILE_PATH} for security threats...\n")

            while True:
                line = file.readline()
                if not line:
                    time.sleep(1)  # Wait for new log entries
                    continue
                
                # Check for suspicious patterns
                for pattern in SUSPICIOUS_PATTERNS:
                    if pattern.lower() in line.lower():
                        print(f"⚠️ ALERT: Suspicious Activity Detected → {line.strip()}")

    except FileNotFoundError:
        print(f"❌ Error: Log file '{LOG_FILE_PATH}' not found! Please provide a valid log file.")

if __name__ == "__main__":
    monitor_log()
