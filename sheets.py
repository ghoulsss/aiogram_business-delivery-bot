import os
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dotenv import load_dotenv
import gspread


load_dotenv()
spreadsheet_id = os.getenv("spreadsheet_id")

credentials = service_account.Credentials.from_service_account_file(
    "key.json", scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
if not credentials.valid:
    credentials.refresh(Request())

service = build("sheets", "v4", credentials=credentials)

users = (
    service.spreadsheets()
    .values()
    .get(spreadsheetId=spreadsheet_id, range="Пользователи")
    .execute()
    .get("values", [])
)


def get_credentials():
    if not credentials.valid:
        credentials.refresh()

    return credentials


super_user = int(users[0][1])
admin_sklada = int(users[1][1])
courier = int(users[2][1])

gc = gspread.service_account(filename="key.json")

sh = gc.open("доставка")

# # -----------------------------------
# worksheet = sh.worksheet("Пользователи")
# users = worksheet.get_all_records()
# print(f"Пользователи обновлены {users}")
