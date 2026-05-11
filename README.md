````markdown
# 🧠 Advanced Note-Taking Data Structure System

> A modern terminal-based note-taking application built with Python using advanced data structure concepts such as Doubly Linked Lists, Multi-Tag Relationships, and Circular Buffers.

---

## 📌 Project Overview

This project was developed as part of a **Data Structures course assignment**.  
The main goal of the project is to demonstrate the implementation of multiple advanced data structures inside a real-world mini application.

Unlike a regular note application that only uses Python lists, this system was specifically designed to implement:

- ✅ Doubly Linked Lists
- ✅ Multi-linked Tag Relationships
- ✅ Circular Buffer Activity Tracking
- ✅ Sorted Views
- ✅ Interactive CLI System

---

# ✨ Features

## 📝 Smart Note Management
Create and manage notes interactively through a terminal-based interface.

Each note contains:
- Unique ID
- Title
- Content
- Multiple Tags
- Created Timestamp
- Updated Timestamp
- Pin Status
- Archive Status

---

## 🔗 Doubly Linked List System

The application uses a custom-built **Doubly Linked List** implementation instead of Python's built-in list.

### Supported Views

### ⏱ Chronological View
Notes are automatically sorted by creation time.

### 🔤 Alphabetical View
Notes are automatically sorted alphabetically by title.

### Features
- Forward traversal
- Backward traversal
- Dynamic insertion
- Node deletion
- Sorted insertion logic

---

## 🏷 Multi-Tag Relationship System

Each note can contain multiple tags.

Example:

```text
Note:
"Learn Python"

Tags:
python, coding, university
````

The system maintains relationships between:

* One note → multiple tags
* One tag → multiple notes

### Tag Features

* Tag search
* Tag statistics
* Most-used tag tracking
* Dynamic tag cleanup

---

## 🔄 Circular Buffer Activity Tracking

The system uses a real **Circular Buffer** implementation to store recent activities.

### Example Activities

* Added note
* Deleted note
* Edited note
* Archived note

### Circular Buffer Features

* Fixed-size memory
* Automatic overwrite
* Head/Tail pointer movement
* Raw buffer visualization
* Buffer status monitoring

---

# 🧩 Data Structures Used

| Data Structure            | Purpose                                 |
| ------------------------- | --------------------------------------- |
| Doubly Linked List        | Chronological & alphabetical note views |
| Multi-linked Relationship | Tag-to-note mapping                     |
| Circular Buffer           | Recent sync/activity history            |
| Dictionary / Hash Map     | Fast tag lookup                         |
| Node-based Structure      | Manual linked list implementation       |

---

# 📂 Project Structure

```text
note-taking-data-structure/
│
├── main.py
├── note.py
├── linked_list.py
├── tag_manager.py
├── circular_buffer.py
├── README.md
│
└── screenshots/
```

---

# 📄 File Descriptions

## `main.py`

Main application controller and interactive CLI system.

---

## `note.py`

Contains the `Note` class and note-related functionalities.

---

## `linked_list.py`

Implements:

* Node structure
* Doubly Linked List
* Sorted insertion
* Traversal logic

---

## `tag_manager.py`

Handles:

* Tag relationships
* Tag searching
* Tag statistics

---

## `circular_buffer.py`

Implements:

* Circular buffer memory
* Activity tracking
* Buffer visualization

---

# ⚙️ How to Run

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/note-taking-data-structure.git
```

---

## 2️⃣ Open Project Folder

```bash
cd note-taking-data-structure
```

---

## 3️⃣ Run Application

```bash
python main.py
```

---

# 🖥 Example Main Menu

```text
🧠 ADVANCED NOTE-TAKING DATA STRUCTURE SYSTEM

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
```

---

# 📸 Screenshots

## 🏠 Main Menu

![Main Menu](screenshots/main-menu.png)

---

## ⏱ Chronological View

![Chronological View](screenshots/chronological-view.png)

---

## 🔍 Tag Search

![Tag Search](screenshots/tag-search.png)

---

## 🔄 Activity History

![Activity History](screenshots/activity-history.png)

---

## 🧠 Raw Circular Buffer

![Raw Buffer](screenshots/raw-buffer.png)

---

# 🧪 Example Data Flow

```text
User Input
   ↓
Create Note Object
   ↓
Insert into Chronological Linked List
   ↓
Insert into Alphabetical Linked List
   ↓
Connect Tags using TagManager
   ↓
Record Activity using Circular Buffer
```

---

# 📊 System Highlights

## ✅ Real Doubly Linked List

This project does NOT rely solely on Python lists for note organization.

The linked list was manually implemented using:

* Nodes
* Prev pointers
* Next pointers

---

## ✅ Real Circular Buffer

The activity system uses:

* Head pointer
* Tail pointer
* Circular movement
* Automatic overwrite logic

instead of using:

```python
list.pop(0)
```

---

## ✅ Interactive Terminal Experience

The application provides:

* Interactive menu navigation
* Structured terminal output
* Clean dashboard displays

---

# 🎯 Educational Objectives

This project helps demonstrate understanding of:

* Dynamic data structures
* Pointer-based navigation
* Sorted linked insertion
* Circular memory management
* Data relationship mapping

---

# 🚀 Possible Future Improvements

* File/database persistence
* GUI interface
* Note editing system
* User authentication
* Real cloud synchronization
* Priority-based note sorting

---

# 👨‍💻 Author

Developed for:
**Data Structures Course Assignment**

Using:

* Python 3
* Object-Oriented Programming
* Custom Data Structure Implementations

---

# 📜 License

This project is intended for educational purposes only.

```
```

