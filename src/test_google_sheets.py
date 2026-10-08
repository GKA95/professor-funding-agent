
from google_sheets import get_spreadsheet

spreadsheet = get_spreadsheet()

print("Google Sheets connection successful!")
print("Spreadsheet title:", spreadsheet.title)

for worksheet in spreadsheet.worksheets():
    print("Found worksheet:", worksheet.title)
