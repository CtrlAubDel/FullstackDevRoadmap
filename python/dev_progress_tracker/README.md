# Dev Progress Tracker (Python)

A simple CLI tool to log daily programming language, growth topic, and progress summary into a JSON file.  
Helps track my journey and reinforce consistent learning habits.

## Features
- Add a new log for today's date (overwrites if already exists)
- View all saved logs sorted by date
- Search entries by date or keyword (language, topic, or summary)
- Confirm before overwriting existing logs

## How to Use

1. Run the program:
   ```bash
   python tracker.py
   ```

2. Choose a mode when prompted:
   - `add` → Create or overwrite today’s log
   - `view` → Display all past logs
   - `search` → Search logs by date or keyword

3. Data is saved in: `log.json` (in the same directory as the script)

## File Example

Sample `log.json` structure:

```json
{
  "2025-05-06": {
    "language": "Python",
    "topic": "File I/O and CLI menus",
    "summary": "Implemented logic to save logs to a JSON file and added a CLI mode selector."
  }
}
```

## Tech Used
- Python 3.10+
- Built-in `json`, `datetime`, and `os` modules
- No external libraries required

## Author
Created by Aubrey Corcoran as part of a fullstack developer learning roadmap.