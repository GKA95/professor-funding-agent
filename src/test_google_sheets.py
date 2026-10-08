import os
import sys
import sysconfig
import importlib.util

# Force Python to use the real standard-library queue module.
stdlib = sysconfig.get_paths()["stdlib"]
queue_file = os.path.join(stdlib, "queue.py")

spec = importlib.util.spec_from_file_location("queue", queue_file)
queue = importlib.util.module_from_spec(spec)
spec.loader.exec_module(queue)

sys.modules["queue"] = queue

print("Queue module loaded from:", queue_file)
print("LifoQueue available:", hasattr(queue, "LifoQueue"))

# Make src importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from google_sheets import get_spreadsheet

spreadsheet = get_spreadsheet()

print("Google Sheets connection successful!")
print("Spreadsheet title:", spreadsheet.title)

for worksheet in spreadsheet.worksheets():
    print("Found worksheet:", worksheet.title)
