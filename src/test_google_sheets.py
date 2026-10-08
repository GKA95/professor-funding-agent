import os
import sys

# Remove the src directory from the import path temporarily.
src_dir = os.path.dirname(os.path.abspath(__file__))
if src_dir in sys.path:
    sys.path.remove(src_dir)

# Test Python's standard queue module.
import queue

print("Python queue module:", queue.__file__)
print("Has LifoQueue:", hasattr(queue, "LifoQueue"))

if not hasattr(queue, "LifoQueue"):
    raise RuntimeError(
        f"Python is loading the wrong queue module: {queue.__file__}"
    )

# Now load our Google Sheets connector.
sys.path.insert(0, src_dir)

from google_sheets import get_spreadsheet

spreadsheet = get_spreadsheet()

print("Google Sheets connection successful!")
print("Spreadsheet title:", spreadsheet.title)

for worksheet in spreadsheet.worksheets():
    print("Found worksheet:", worksheet.title)
