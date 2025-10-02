# ③ Local Modules
from src.config import load_settings
from src.daelim.gw.inbox_scraper import scrape_inbox
from src.daelim.pt.login_flow import login_to_portal
from src.daelim.pt.menu_navigation import go_to_inbox
from src.infra.browser.chrome_driver import build_driver
from src.infra.service.notion import append_to_notion
from src.infra.service.spreadsheet import append_to_spreadsheet

def main() -> None:

    """메인 자동화 프로세스 실행"""

    # 설정 로드 및 드라이버 초기화
    settings = load_settings()
    driver = build_driver(settings)

    # 포털 로그인 후 수신접수함으로 이동
    driver = login_to_portal(driver, settings)
    driver = go_to_inbox(driver)

    # 수신접수함에서 문서 스크래핑
    DocList = scrape_inbox(driver)

    # 스프레드시트 및 노션DB에 데이터 연동
    if DocList:
        append_to_spreadsheet(settings, DocList)
        append_to_notion(settings, DocList)
    else:
        print("⚠️ 도착한 문서가 없습니다.")

    # 작업 완료 및 브라우저 종료
    input("🔍 작업 완료! Enter 키를 누르면 브라우저가 종료됩니다...")
    driver.quit()

    return None
