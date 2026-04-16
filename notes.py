import json
import os
import datetime

NOTES_FILE = 'notes.json'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            data = json.load(f)
            # Handle old format (list of strings) by converting to new format
            if data and isinstance(data[0], str):
                now = datetime.datetime.now().isoformat()
                return [{'content': note, 'timestamp': now} for note in data]
            return data
    return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=4)

def add_note(notes):
    print("Enter your note (multi-line). Type 'END' on a new line to finish:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    content = '\n'.join(lines)
    timestamp = datetime.datetime.now().isoformat()
    notes.append({'content': content, 'timestamp': timestamp})
    save_notes(notes)
    print("✅ Note added successfully!")

def view_notes(notes):
    if not notes:
        print("📝 No notes found.")
        return
    print("\n" + "="*50)
    print("📋 ALL NOTES")
    print("="*50)
    for i, note in enumerate(notes, 1):
        print(f"\n--- Note {i} ---")
        print(f"🕒 Timestamp: {note['timestamp']}")
        print(f"📄 Content:\n{note['content']}")
        print("-" * 30)

def delete_note(notes):
    if not notes:
        print("📝 No notes to delete.")
        return
    view_notes(notes)
    try:
        idx = int(input("Enter the number of the note to delete: ")) - 1
        if 0 <= idx < len(notes):
            del notes[idx]
            save_notes(notes)
            print("🗑️ Note deleted successfully!")
        else:
            print("❌ Invalid index. Please enter a valid note number.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def search_notes(notes):
    if not notes:
        print("📝 No notes to search.")
        return
    keyword = input("🔍 Enter keyword to search: ").lower()
    matches = []
    for i, note in enumerate(notes):
        if keyword in note['content'].lower():
            matches.append((i+1, note))
    if not matches:
        print("🔍 No notes found matching the keyword.")
        return
    print(f"🔍 Found {len(matches)} matching note(s):")
    for idx, note in matches:
        print(f"\n--- Note {idx} ---")
        print(f"🕒 Timestamp: {note['timestamp']}")
        print(f"📄 Content:\n{note['content']}")
        print("-" * 30)

def main():
    notes = load_notes()
    print("🎉 Welcome to the Enhanced Notes App!")
    while True:
        print("\n" + "="*40)
        print("📝 NOTES APP MENU")
        print("="*40)
        print("1. ➕ Add a new note")
        print("2. 👀 View all notes")
        print("3. 🗑️  Delete a note")
        print("4. 🔍 Search notes")
        print("5. 🚪 Exit")
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_note(notes)
        elif choice == '2':
            view_notes(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            search_notes(notes)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()