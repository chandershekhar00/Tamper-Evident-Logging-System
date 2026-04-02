import hashlib
import json
from datetime import datetime
import os

class LogEntry:
    def __init__(self, index, timestamp, event_type, description, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.event_type = event_type
        self.description = description
        self.previous_hash = previous_hash
        self.current_hash = self.calculate_hash()

    def calculate_hash(self):
        data = f"{self.index}{self.timestamp}{self.event_type}{self.description}{self.previous_hash}"
        return hashlib.sha256(data.encode()).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "event_type": self.event_type,
            "description": self.description,
            "previous_hash": self.previous_hash,
            "current_hash": self.current_hash
        }


class TamperEvidentLog:
    def __init__(self, filename="logs.json"):
        self.filename = filename
        self.logs = []
        if os.path.exists(self.filename):
            self.load()
        else:
            self._create_genesis()
            self.save()

    def _create_genesis(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        genesis = LogEntry(0, timestamp, "GENESIS", "System initialized", "0")
        self.logs.append(genesis)

    def add_log(self, event_type, description):
        last_log = self.logs[-1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        entry = LogEntry(
            index=len(self.logs),
            timestamp=timestamp,
            event_type=event_type,
            description=description,
            previous_hash=last_log.current_hash
        )
        self.logs.append(entry)
        self.save()
        print(f"Log {entry.index} added successfully")

    def verify_integrity(self):
        for i in range(1, len(self.logs)):
            current = self.logs[i]
            previous = self.logs[i - 1]

            if current.current_hash != current.calculate_hash():
                return f"Tampering detected at log {i}: data modified"

            if current.previous_hash != previous.current_hash:
                return f"Tampering detected at log {i}: chain broken (deletion or reordering)"

        return "All logs are intact"

    def save(self):
        data = [log.to_dict() for log in self.logs]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        with open(self.filename, "r") as f:
            data = json.load(f)

        self.logs = []
        for item in data:
            entry = LogEntry(
                item["index"],
                item["timestamp"],
                item["event_type"],
                item["description"],
                item["previous_hash"]
            )
            entry.current_hash = item["current_hash"]
            self.logs.append(entry)

    def display_logs(self):
        for log in self.logs:
            print("-" * 50)
            print(f"Index       : {log.index}")
            print(f"Timestamp   : {log.timestamp}")
            print(f"Event Type  : {log.event_type}")
            print(f"Description : {log.description}")
            print(f"Prev Hash   : {log.previous_hash}")
            print(f"Hash        : {log.current_hash}")
        print("-" * 50)


def main():
    system = TamperEvidentLog()

    while True:
        print("\n1. Add Log Entry")
        print("2. Verify Log Integrity")
        print("3. Display Logs")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            event = input("Event Type: ").strip()
            description = input("Description: ").strip()
            system.add_log(event, description)

        elif choice == "2":
            print(system.verify_integrity())

        elif choice == "3":
            system.display_logs()

        elif choice == "4":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()