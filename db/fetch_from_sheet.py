import gspread as gs
from oauth2client.service_account import ServiceAccountCredentials

scope = [
  'https://spreadsheets.google.com/feeds',
  'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gs.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
# sheet = client.open("test").sheet1

# Extract and print all of the values
'''
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
'''

class SheetData:
  def __init__(self, link):
    self.link = link

  def get_sheet(self):
    return client.open("test").sheet1.get_all_records()