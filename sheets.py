import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials


load_dotenv()
spreadsheet_id = os.getenv("spreadsheet_id")

credentials = service_account.Credentials.from_service_account_file(
    "key.json", scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
service = build("sheets", "v4", credentials=credentials)

users = (
    service.spreadsheets()
    .values()
    .get(spreadsheetId=spreadsheet_id, range="Пользователи")
    .execute()
    .get("values", [])
)

super_user = int(users[0][1])
admin_sklada = int(users[1][1])
courier = int(users[2][1])

gc = gspread.service_account(filename="key.json")

sh = gc.open("доставка")
