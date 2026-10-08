import json
import os

import gspread
from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def get_client():
    credentials_json = os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]

    credentials_info = json.loads(credentials_json)

    credentials = Credentials.from_service_account_info(
        credentials_info,
        scopes=SCOPES,
    )

    return gspread.authorize(credentials)


def get_spreadsheet():
    client = get_client()

    spreadsheet_id = os.environ["GOOGLE_SHEET_ID"]

    return client.open_by_key(spreadsheet_id)


def get_worksheet(sheet_name):
    spreadsheet = get_spreadsheet()

    return spreadsheet.worksheet(sheet_name)


def get_all_professors():
    worksheet = get_worksheet("Professors")

    return worksheet.get_all_records()


def get_email_queue():
    worksheet = get_worksheet("Email Queue")

    return worksheet.get_all_records()


def get_settings():
    worksheet = get_worksheet("Settings")

    records = worksheet.get_all_records()

    return {
        row["Setting"]: row["Value"]
        for row in records
    }
