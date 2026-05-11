from datetime import datetime
import uuid


class Note:
    def __init__(self, title, content, tags):
        self.id = str(uuid.uuid4())[:8]

        self.title = title.strip()
        self.content = content.strip()

        self.tags = [tag.strip().lower() for tag in tags]

        self.created_at = datetime.now()
        self.updated_at = self.created_at

        self.is_pinned = False
        self.is_archived = False

    def edit_note(self, new_title=None, new_content=None):
        if new_title:
            self.title = new_title.strip()

        if new_content:
            self.content = new_content.strip()

        self.updated_at = datetime.now()

    def add_tag(self, tag):
        tag = tag.strip().lower()

        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        tag = tag.strip().lower()

        if tag in self.tags:
            self.tags.remove(tag)

    def pin_note(self):
        self.is_pinned = True

    def archive_note(self):
        self.is_archived = True

    def display(self):
        print("\n" + "=" * 50)
        print("📝 NOTE DETAILS")
        print("=" * 50)

        print(f"ID           : {self.id}")
        print(f"Title        : {self.title}")
        print(f"Content      : {self.content}")

        print(f"Tags         : {', '.join(self.tags)}")

        print(f"Created At   : {self.created_at.strftime('%d-%m-%Y %H:%M:%S')}")
        print(f"Updated At   : {self.updated_at.strftime('%d-%m-%Y %H:%M:%S')}")

        print(f"Pinned       : {'Yes' if self.is_pinned else 'No'}")
        print(f"Archived     : {'Yes' if self.is_archived else 'No'}")

        print("=" * 50)