import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv


load_dotenv()
spreadsheet_id = os.getenv("spreadsheet_id")

credentials = service_account.Credentials.from_service_account_file(
    "key.json", scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
service = build("sheets", "v4", credentials=credentials)


data_sheet = (
    service.spreadsheets()
    .values()
    .get(spreadsheetId=spreadsheet_id, range="Лист1")
    .execute()
    .get("values", [])
)

super_user = int(data_sheet[0][1])
admin_sklada = int(data_sheet[1][1])
courier = int(data_sheet[2][1])
