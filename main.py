from note import Note
from linked_list import DoublyLinkedList
from tag_manager import TagManager
from circular_buffer import CircularBuffer


# =========================
# INITIALIZE SYSTEM
# =========================

chronological_list = DoublyLinkedList(mode="chronological")
alphabetical_list = DoublyLinkedList(mode="alphabetical")

tag_manager = TagManager()

history_buffer = CircularBuffer(capacity=10)


# =========================
# HELPER FUNCTIONS
# =========================

def print_banner():
    print("\n" + "=" * 70)
    print("🧠 ADVANCED NOTE-TAKING DATA STRUCTURE SYSTEM")
    print("=" * 70)
    print("Features:")
    print("• Doubly Linked List")
    print("• Multi-Tag Relationship")
    print("• Circular Buffer Activity Tracking")
    print("=" * 70)


def pause():
    input("\nPress Enter to continue...")


def create_note():
    print("\n📝 CREATE NEW NOTE")

    title = input("Title   : ")
    content = input("Content : ")

    raw_tags = input("Tags (comma separated) : ")
    tags = [tag.strip() for tag in raw_tags.split(",")]

    note = Note(title, content, tags)

    chronological_list.insert(note)
    alphabetical_list.insert(note)

    tag_manager.add_note_tags(note)

    history_buffer.add_action(f"Added note: {title}")

    print("\n✅ Note added successfully!")


def view_chronological():
    chronological_list.display_forward()


def view_alphabetical():
    alphabetical_list.display_forward()


def search_by_tag():
    tag = input("\nEnter tag to search : ")

    tag_manager.display_notes_by_tag(tag)


def show_all_tags():
    tag_manager.display_all_tags()


def show_statistics():
    print("\n" + "=" * 70)
    print("📊 SYSTEM STATISTICS")
    print("=" * 70)

    print(f"Total Notes          : {chronological_list.count_notes()}")
    print(f"Total Tags           : {tag_manager.total_tags()}")

    most_used = tag_manager.get_most_used_tag()

    if most_used:
        print(f"Most Used Tag        : #{most_used[0]} ({len(most_used[1])} notes)")
    else:
        print("Most Used Tag        : None")

    latest = history_buffer.get_latest_action()

    if latest:
        print(f"Latest Activity      : {latest['action']}")
    else:
        print("Latest Activity      : None")

    print("=" * 70)


def show_history():
    history_buffer.display_history()


def show_buffer_status():
    history_buffer.display_buffer_status()


def show_raw_buffer():
    history_buffer.display_raw_buffer()


def search_by_title():
    keyword = input("\nEnter title keyword : ")

    results = chronological_list.search_by_title(keyword)

    print("\n" + "=" * 70)
    print("🔍 SEARCH RESULTS")
    print("=" * 70)

    if not results:
        print("No matching notes found.")

    else:
        for index, note in enumerate(results, start=1):
            print(f"\n[{index}] {note.title}")
            print(f"Tags      : {', '.join(note.tags)}")
            print(f"Created   : {note.created_at.strftime('%d-%m-%Y %H:%M:%S')}")

    print("=" * 70)


def delete_note():
    note_id = input("\nEnter Note ID to delete : ")

    success1 = chronological_list.delete_note(note_id)
    success2 = alphabetical_list.delete_note(note_id)

    if success1 and success2:
        history_buffer.add_action(f"Deleted note ID: {note_id}")

        print("\n✅ Note deleted successfully!")

    else:
        print("\n❌ Note not found.")


# =========================
# MAIN LOOP
# =========================

while True:
    print_banner()

    print("""
[1] Create Note
[2] View Notes (Chronological)
[3] View Notes (Alphabetical)
[4] Search Notes by Tag
[5] Search Notes by Title
[6] Show All Tags
[7] Show Statistics
[8] Show Activity History
[9] Show Buffer Status
[10] Show Raw Circular Buffer
[11] Delete Note
[0] Exit
""")

    choice = input("Select menu : ")

    if choice == "1":
        create_note()
        pause()

    elif choice == "2":
        view_chronological()
        pause()

    elif choice == "3":
        view_alphabetical()
        pause()

    elif choice == "4":
        search_by_tag()
        pause()

    elif choice == "5":
        search_by_title()
        pause()

    elif choice == "6":
        show_all_tags()
        pause()

    elif choice == "7":
        show_statistics()
        pause()

    elif choice == "8":
        show_history()
        pause()

    elif choice == "9":
        show_buffer_status()
        pause()

    elif choice == "10":
        show_raw_buffer()
        pause()

    elif choice == "11":
        delete_note()
        pause()

    elif choice == "0":
        print("\n👋 Exiting program...")
        print("Thank you for using the system!")
        break

    else:
        print("\n❌ Invalid menu choice.")
        pause()