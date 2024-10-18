import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

spreadsheet_id = os.getenv('spreadsheet_id')

credentials = service_account.Credentials.from_service_account_file("key.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
service = build("sheets", "v4", credentials=credentials)

request = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False)
sheet_props = request.execute()

print(sheet_props["properties"]["title"])
