import os
import sys
import sysconfig
import importlib.util

# Load Python's standard-library queue module explicitly.
stdlib = sysconfig.get_paths()["stdlib"]
queue_file = os.path.join(stdlib, "queue.py")

spec = importlib.util.spec_from_file_location("queue", queue_file)
queue = importlib.util.module_from_spec(spec)
spec.loader.exec_module(queue)

sys.modules["queue"] = queue

# Import Google Sheets connector.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from google_sheets import get_spreadsheet


spreadsheet = get_spreadsheet()

print("Google Sheets connection successful!")
print("Spreadsheet title:", spreadsheet.title)

for worksheet in spreadsheet.worksheets():
    print("Found worksheet:", worksheet.title)
