import json
from datetime import date
import os

# Path for log file
LOG_FILE = os.path.join(os.path.dirname(__file__), "log.json")

# Add entry function
def add_entry():
    today = str(date.today())
    
    # User prompts
    language = input("What programming language did you study today? ")
    topic = input("What topic did you focus on? ")
    summary = input("Write a short summary of what you learned: ")
    
    # User entries
    entry = {
        "language": language,
        "topic": topic,
        "summary": summary
    }
    
    # Load existing data
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    else:
        logs = {}
        
    # Add or overwrite today's entry
    logs[today] = entry

    # Save back to file
    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=2)

    print(f"\nSaved log for {today} to: {LOG_FILE}")

# View entries function
def view_entries():
    try:
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo logs found.")
        return

    for date_key in sorted(logs.keys()):
        entry = logs[date_key]
        print(f"\n{date_key}")
        print(f"Language: {entry['language']}")
        print(f"Topic:    {entry['topic']}")
        print(f"Summary:  {entry['summary']}")

# Search entries function
def search_entries():
    try:
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo logs found.")
        return

    while True:
        query = input("\nEnter a date (YYYY-MM-DD) or keyword to search: ").strip().lower()

        results = []
        for date_key, entry in logs.items():
            if (
                query in date_key.lower() or
                query in entry['language'].lower() or
                query in entry['topic'].lower() or
                query in entry['summary'].lower()
            ):
                results.append((date_key, entry))

        if not results:
            print("\nNo matching entries found.")
        else:
            print(f"\nFound {len(results)} matching entr{'y' if len(results)==1 else 'ies'}:")
            for date_key, entry in sorted(results):
                print(f"\n{date_key}")
                print(f"Language: {entry['language']}")
                print(f"Topic:    {entry['topic']}")
                print(f"Summary:  {entry['summary']}")

        again = input("\nSearch for another entry? (y/n): ").strip().lower()
        if again != "y":
            print("\nReturning to main menu.")
            break

# CLI Menu Entry Point
if __name__ == "__main__":
    mode = input("\nType 'add' to log a new entry, 'search' to find specific entries, or 'view' to see all past entries: ").strip().lower()

    if mode == "add":
        today = str(date.today())

        try:
            with open(LOG_FILE, "r") as file:
                logs = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            logs = {}

        if today in logs:
            print("\nYou have already logged an entry today.")
        else:
            print("\nYou have not logged an entry for today yet.")

        print("\nWarning: If you proceed, it will overwrite any existing log for today.\n")

        confirm = input("Do you want to continue? (y/n): ").strip().lower()
        if confirm == 'y':
            add_entry()
        else:
            print("\nLog entry canceled.")

    elif mode == "search":
        search_entries()
    elif mode == "view":
        view_entries()
    else:
        print("Invalid option. Please choose 'add', 'search', or 'view'.")
