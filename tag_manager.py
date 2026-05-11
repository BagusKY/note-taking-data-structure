class TagManager:
    def __init__(self):
        # Struktur:
        # {
        #   "python": [note1, note2],
        #   "coding": [note1]
        # }
        self.tag_map = {}

    def add_note_tags(self, note):
        for tag in note.tags:

            # Jika tag belum ada
            if tag not in self.tag_map:
                self.tag_map[tag] = []

            # Hindari duplicate note
            if note not in self.tag_map[tag]:
                self.tag_map[tag].append(note)

    def remove_note(self, note):
        for tag in note.tags:

            if tag in self.tag_map:

                if note in self.tag_map[tag]:
                    self.tag_map[tag].remove(note)

                # Hapus tag kosong
                if len(self.tag_map[tag]) == 0:
                    del self.tag_map[tag]

    def search_by_tag(self, tag):
        tag = tag.lower().strip()

        if tag in self.tag_map:
            return self.tag_map[tag]

        return []

    def display_all_tags(self):
        print("\n" + "=" * 60)
        print("🏷️ ALL TAGS")
        print("=" * 60)

        if not self.tag_map:
            print("No tags available.")
            return

        for index, tag in enumerate(sorted(self.tag_map.keys()), start=1):
            total_notes = len(self.tag_map[tag])

            print(f"\n[{index}] #{tag}")
            print(f"Connected Notes : {total_notes}")

        print("\n" + "=" * 60)

    def display_notes_by_tag(self, tag):
        notes = self.search_by_tag(tag)

        print("\n" + "=" * 60)
        print(f"🔍 SEARCH RESULT FOR TAG: #{tag}")
        print("=" * 60)

        if not notes:
            print("No notes found.")
            return

        for index, note in enumerate(notes, start=1):
            print(f"\n[{index}] {note.title}")
            print(f"Content    : {note.content}")
            print(f"Tags       : {', '.join(note.tags)}")
            print(f"Created At : {note.created_at.strftime('%d-%m-%Y %H:%M:%S')}")

        print("\n" + "=" * 60)

    def display_tag_statistics(self):
        print("\n" + "=" * 60)
        print("📊 TAG STATISTICS")
        print("=" * 60)

        if not self.tag_map:
            print("No statistics available.")
            return

        sorted_tags = sorted(
            self.tag_map.items(),
            key=lambda item: len(item[1]),
            reverse=True
        )

        for index, (tag, notes) in enumerate(sorted_tags, start=1):
            print(f"{index}. #{tag} → {len(notes)} notes")

        print("\n" + "=" * 60)

    def get_most_used_tag(self):
        if not self.tag_map:
            return None

        return max(
            self.tag_map.items(),
            key=lambda item: len(item[1])
        )

    def total_tags(self):
        return len(self.tag_map)