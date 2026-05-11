from datetime import datetime


class CircularBuffer:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buffer = [None] * capacity

        self.head = 0
        self.tail = 0

        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def add_action(self, action):
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        activity = {
            "action": action,
            "timestamp": timestamp
        }

        # Masukkan data baru
        self.buffer[self.tail] = activity

        # Geser tail circular
        self.tail = (self.tail + 1) % self.capacity

        # Jika penuh → overwrite oldest
        if self.is_full():
            self.head = (self.head + 1) % self.capacity
        else:
            self.size += 1

    def display_history(self):
        print("\n" + "=" * 65)
        print("🔄 RECENT SYNC & ACTIVITY HISTORY")
        print("=" * 65)

        if self.is_empty():
            print("No recent activities.")
            return

        index = self.head
        counter = 1

        for _ in range(self.size):
            activity = self.buffer[index]

            print(f"\n[{counter}] {activity['action']}")
            print(f"Timestamp : {activity['timestamp']}")

            index = (index + 1) % self.capacity
            counter += 1

        print("\n" + "=" * 65)

    def get_latest_action(self):
        if self.is_empty():
            return None

        latest_index = (self.tail - 1) % self.capacity

        return self.buffer[latest_index]

    def clear_history(self):
        self.buffer = [None] * self.capacity

        self.head = 0
        self.tail = 0
        self.size = 0

    def display_buffer_status(self):
        print("\n" + "=" * 65)
        print("📦 BUFFER STATUS")
        print("=" * 65)

        print(f"Capacity        : {self.capacity}")
        print(f"Current Size    : {self.size}")
        print(f"Head Pointer    : {self.head}")
        print(f"Tail Pointer    : {self.tail}")

        print(f"Buffer Full     : {'Yes' if self.is_full() else 'No'}")
        print(f"Buffer Empty    : {'Yes' if self.is_empty() else 'No'}")

        print("=" * 65)

    def display_raw_buffer(self):
        print("\n" + "=" * 65)
        print("🧠 RAW CIRCULAR BUFFER MEMORY")
        print("=" * 65)

        for index, item in enumerate(self.buffer):

            if item is None:
                print(f"[{index}] Empty")
            else:
                print(f"[{index}] {item['action']}")

        print("=" * 65)