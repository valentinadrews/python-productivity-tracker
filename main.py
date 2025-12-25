import json
from datetime import datetime

class ProductivityTracker:
    def __init__(self):
        self.data_file = 'database.json'
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.history = json.load(f)
        except FileNotFoundError:
            self.history = []

    def log_status(self, sleep_hours, social_battery):
        entry = {
            "date": str(datetime.now()),
            "sleep_hours": sleep_hours,
            "social_battery": social_battery,
            "status": "Critical" if sleep_hours < 5 else "Optimal"
        }
        self.history.append(entry)
        self.save_data()
        print(f"Registered state: {entry['status']}")

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.history, f, indent=4)

if __name__ == "__main__":
    tracker = ProductivityTracker()
    # example:
    tracker.log_status(sleep_hours=2, social_battery=10)