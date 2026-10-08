import sys
import os

print("Python:", sys.version)
print("Current directory:", os.getcwd())
print("sys.path:")
for path in sys.path:
    print("  ", path)

import queue

print("QUEUE MODULE:")
print("  file:", getattr(queue, "__file__", "UNKNOWN"))
print("  has LifoQueue:", hasattr(queue, "LifoQueue"))

if not hasattr(queue, "LifoQueue"):
    raise RuntimeError(
        "WRONG QUEUE MODULE LOADED. "
        f"Python loaded queue from: {getattr(queue, '__file__', 'UNKNOWN')}"
    )

from google_sheets import get_spreadsheet

spreadsheet = get_spreadsheet()

print("Google Sheets connection successful!")
print("Spreadsheet title:", spreadsheet.title)

for worksheet in spreadsheet.worksheets():
    print("Found worksheet:", worksheet.title)
