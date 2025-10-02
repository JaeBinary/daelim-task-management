# ② Third-party Library
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# ③ Local Modules
from src.config import Settings

def append_to_spreadsheet(settings: Settings, DocList: list) -> None:

    """스프레드시트에 연동"""

    # 서비스 계정 인증
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file(settings.credentials_path, scopes=scopes)

    # 서비스 생성
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # 데이터 추가 요청
    request = sheet.values().append(
        spreadsheetId = settings.spreadsheet_id,
        range = 'AI시스템과!A2',
        valueInputOption = 'USER_ENTERED',
        insertDataOption = 'INSERT_ROWS',
        body = {'values': DocList}
    )
    response = request.execute()

    # 업데이트된 행 수 확인
    updated_rows = response.get('updates', {}).get('updatedRows', 0)
    if updated_rows > 0:
        print(f"✅ {updated_rows}행 추가 완료 : Google Sheets")
    else:
        print("❌ 추가 실패 : Google Sheets")

    return None
