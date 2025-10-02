# ① Standard Library
import os
from dataclasses import dataclass
from pathlib import Path

# ② Third-party Library
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

@dataclass(frozen=True)
class Settings:

    """불변 설정 객체 - .env 파일 기반 환경변수"""

    url: str
    user_id: str
    user_pw: str
    chrome_driver_path: Path
    spreadsheet_id: str
    credentials_path: Path
    notion_token: str
    db_id: str

def load_settings() -> Settings:

    """환경변수 로드 및 타입 변환하여 Settings 객체 생성"""

    load_dotenv()
    return Settings(
        url=os.getenv("URL", "").strip(),
        user_id=os.getenv("USER_ID", "").strip(),
        user_pw=os.getenv("USER_PW", "").strip(),
        chrome_driver_path=Path(os.getenv("CHROME_DRIVER_PATH", "drivers/chromedriver.exe")).resolve(),
        spreadsheet_id=os.getenv("SPREADSHEET_ID","").strip(),
        credentials_path=Path(os.getenv("CREDENTIALS_PATH", "credentials/credentials.json")).resolve(),
        notion_token=os.getenv("NOTION_TOKEN", "").strip(),
        db_id=os.getenv("DB_ID", "").strip()
    )
