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


def get_credentials():
    if not credentials.valid:
        credentials.refresh()

    return credentials


roles = {"Супер юзер": [], "Админ склада": [], "Курьер": []}


async def get_users():
    worksheet = sh.worksheet("Пользователи")
    users = worksheet.get_all_records()
    for row in users:
        role = row["Роль"]
        user_id = row["id"]
        if role in roles:
            roles[role].append(user_id)


gc = gspread.service_account(filename="key.json")

sh = gc.open("доставка")
