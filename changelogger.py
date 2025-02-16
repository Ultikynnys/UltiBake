import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re
import os

CHANGELOG_FILE = "Changelogs.md"

def load_last_entry():
    """
    Reads the CHANGELOG_FILE and returns a tuple (version, title, changes)
    extracted from the last changelog entry. If no valid entry is found,
    returns empty strings.
    
    Expected entry format:
    
      (2 newlines)
      >## {version} - {title} {date}
          * change line 1
          * change line 2
          ...
    """
    if not os.path.exists(CHANGELOG_FILE):
        return "", "", ""
    
    with open(CHANGELOG_FILE, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Use regex to find all changelog entries.
    # This regex finds a header line starting with ">##" and captures everything until the next occurrence.
    # The re.DOTALL flag makes the dot match newlines.
    pattern = re.compile(r"(>## .+?)(?=\n\n>## |\Z)", re.DOTALL)
    entries = pattern.findall(content)
    
    if not entries:
        return "", "", ""
    
    last_entry = entries[-1].strip()
    # Split the entry into header and the rest (changes)
    lines = last_entry.splitlines()
    if not lines:
        return "", "", ""
    
    header_line = lines[0]
    # Expected header format: >## {version} - {title} {date}
    header_match = re.match(r">##\s*(.+?)\s*-\s*(.+?)\s*(\d{2}/\d{2}/\d{4})", header_line)
    if header_match:
        version = header_match.group(1).strip()
        title = header_match.group(2).strip()
    else:
        version = ""
        title = ""
    
    # The remaining lines (if any) should be bullet items with pattern "    * {change}"
    changes_list = []
    for line in lines[1:]:
        bullet_match = re.match(r"\s*\*\s*(.+)", line)
        if bullet_match:
            changes_list.append(bullet_match.group(1).strip())
        else:
            # If the line doesn't match the bullet pattern, add it as-is (or skip)
            changes_list.append(line.strip())
    changes = "\n".join(changes_list)
    return version, title, changes

def append_changelog():
    # Get input values
    version = version_entry.get().strip()
    title = title_entry.get().strip()
    changes_text = changes_textbox.get("1.0", tk.END).strip()
    
    # Validate inputs
    if not version or not title or not changes_text:
        messagebox.showerror("Missing Data", "Please fill in all fields.")
        return
    
    # Get current date in dd/mm/yyyy format
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    # Process changes: split by newline and build bullet list lines
    changes_lines = changes_text.splitlines()
    bullet_lines = "\n".join([f"    * {line.strip()}" for line in changes_lines if line.strip()])
    
    # Format the changelog entry.
    changelog_entry = (
        "\n\n"
        f">## {version} - {title} {current_date}\n"
        f"{bullet_lines}\n"
    )
    
    try:
        with open(CHANGELOG_FILE, "a", encoding="utf-8") as file:
            file.write(changelog_entry)
        messagebox.showinfo("Success", "Changelog entry appended successfully!")
        # Optionally, clear the fields after appending
        version_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)
        changes_textbox.delete("1.0", tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing to file:\n{e}")

# Create main window
root = tk.Tk()
root.title("Changelog Appender")

# Load last entry as placeholder/default values
last_version, last_title, last_changes = load_last_entry()

# Version Label and Entry
version_label = tk.Label(root, text="Version:")
version_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
version_entry = tk.Entry(root, width=30)
version_entry.grid(row=0, column=1, padx=5, pady=5)
if last_version:
    version_entry.insert(0, last_version)

# Title Label and Entry
title_label = tk.Label(root, text="Title:")
title_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
title_entry = tk.Entry(root, width=30)
title_entry.grid(row=1, column=1, padx=5, pady=5)
if last_title:
    title_entry.insert(0, last_title)

# Changes Label and Text widget
changes_label = tk.Label(root, text="Changes (one per line):")
changes_label.grid(row=2, column=0, sticky="ne", padx=5, pady=5)
changes_textbox = tk.Text(root, width=40, height=10)
changes_textbox.grid(row=2, column=1, padx=5, pady=5)
if last_changes:
    changes_textbox.insert("1.0", last_changes)

# Append button
append_button = tk.Button(root, text="Append Changelog", command=append_changelog)
append_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
