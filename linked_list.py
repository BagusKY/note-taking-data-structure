from note import Note


class Node:
    def __init__(self, note):
        self.note = note
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, mode="chronological"):
        self.head = None
        self.tail = None
        self.mode = mode
        self.size = 0

    def is_empty(self):
        return self.head is None

    def insert(self, note):
        new_node = Node(note)

        # Jika list kosong
        if self.is_empty():
            self.head = self.tail = new_node
            self.size += 1
            return

        current = self.head

        while current:
            # MODE CHRONOLOGICAL
            if self.mode == "chronological":
                if note.created_at > current.note.created_at:
                    break

            # MODE ALPHABETICAL
            elif self.mode == "alphabetical":
                if note.title.lower() < current.note.title.lower():
                    break

            current = current.next

        # Insert di akhir
        if current is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        # Insert di awal
        elif current == self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        # Insert di tengah
        else:
            previous = current.prev

            previous.next = new_node
            new_node.prev = previous

            new_node.next = current
            current.prev = new_node

        self.size += 1

    def display_forward(self):
        if self.is_empty():
            print("\n⚠️ No notes available.")
            return

        print("\n" + "=" * 60)
        print(f"📂 DISPLAY MODE: {self.mode.upper()} (FORWARD)")
        print("=" * 60)

        current = self.head
        index = 1

        while current:
            note = current.note

            print(f"\n[{index}] {note.title}")
            print(f"Tags      : {', '.join(note.tags)}")
            print(f"Created   : {note.created_at.strftime('%d-%m-%Y %H:%M:%S')}")
            print(f"Pinned    : {'Yes' if note.is_pinned else 'No'}")

            current = current.next
            index += 1

        print("\n" + "=" * 60)

    def display_backward(self):
        if self.is_empty():
            print("\n⚠️ No notes available.")
            return

        print("\n" + "=" * 60)
        print(f"📂 DISPLAY MODE: {self.mode.upper()} (BACKWARD)")
        print("=" * 60)

        current = self.tail
        index = self.size

        while current:
            note = current.note

            print(f"\n[{index}] {note.title}")
            print(f"Tags      : {', '.join(note.tags)}")
            print(f"Created   : {note.created_at.strftime('%d-%m-%Y %H:%M:%S')}")
            print(f"Pinned    : {'Yes' if note.is_pinned else 'No'}")

            current = current.prev
            index -= 1

        print("\n" + "=" * 60)

    def search_by_title(self, keyword):
        results = []

        current = self.head

        while current:
            if keyword.lower() in current.note.title.lower():
                results.append(current.note)

            current = current.next

        return results

    def delete_note(self, note_id):
        if self.is_empty():
            return False

        current = self.head

        while current:
            if current.note.id == note_id:

                # Jika node tunggal
                if self.head == self.tail:
                    self.head = self.tail = None

                # Jika head
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None

                # Jika tail
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # Jika tengah
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.size -= 1
                return True

            current = current.next

        return False

    def count_notes(self):
        return self.size