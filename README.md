# 📝 Python CLI Notes App

A simple and intuitive command-line notes application built in Python. Keep track of your thoughts, ideas, and reminders right from your terminal.

## ✨ Features

- **Add Notes**: Quickly add new notes to your collection
- **View Notes**: Display all your saved notes with numbered indexing
- **Delete Notes**: Remove notes by their index number
- **Persistent Storage**: Automatically save and load notes from a JSON file
- **Simple Menu Interface**: Easy-to-navigate command-line menu

## 🛠️ Tech Stack

- **Python 3.x** - Core programming language

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/InsightNav/Notes-App.git
   ```

2. **Ensure Python is installed**:
   - This app requires Python 3.x. Check your version:
     ```bash
     python --version
     ```
   - If not installed, download from [python.org](https://www.python.org/downloads/)

3. **Run the application**:
   ```bash
   python notes.py
   ```

## 📖 How to Use

1. **Launch the App**: Run `python notes.py` in your terminal
2. **Navigate the Menu**: Choose from the available options:
   - **1. Add a note**: Enter your note text when prompted
   - **2. View all notes**: See all your saved notes
   - **3. Delete a note**: Enter the number of the note to remove
   - **4. Exit**: Close the application
3. **Notes are automatically saved** to `notes.json` after each operation

## 💡 Example Usage

```
Notes App Menu:
1. Add a note
2. View all notes
3. Delete a note
4. Exit
Choose an option: 1
Enter your note: Remember to buy groceries
Note added.

Notes App Menu:
1. Add a note
2. View all notes
3. Delete a note
4. Exit
Choose an option: 2
1. Remember to buy groceries

Notes App Menu:
1. Add a note
2. View all notes
3. Delete a note
4. Exit
Choose an option: 4
```

## 📁 Project Structure

```
NOTES-APP/
├── notes.py          # Main application script
├── notes.json        # Notes storage file (created automatically)
└── README.md         # Project documentation
```

## 🔮 Future Improvements (or contributors)

- Add timestamps to notes for better organization
- Support multi-line notes for detailed entries
- Implement search functionality to find notes quickly
- Enhance UI with better formatting and colors
- Add categories or tags for note organization
- Export notes to different formats (TXT, CSV)

---

*Built with ❤️ using Python* (Using Copilot 🤖)
