# ② Third-party Library
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# ③ Local Modules
from src.config import Settings

def login_to_portal(driver: WebDriver, settings: Settings) -> WebDriver:

    "포털사이트 로그인"

    # 포털 접속
    driver.get(settings.url)
    print("💻 브라우저가 열렸습니다.")

    # PortalMain 프레임 진입
    driver.switch_to.frame("PortalMain")
    print("☑️  [진입] PortalMain 프레임")

    # 로그인 화면이 바로 안뜰 때 (ex. 수강신청기간)
    if not driver.find_elements(By.ID, "id"):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='학생포털시스템']"))).click()
        print("✅ 학생포털시스템 이미지 클릭 완료")

    # 로그인 정보 입력
    driver.find_element(By.ID, "id").send_keys(settings.user_id)
    driver.find_element(By.ID, "pw").send_keys(settings.user_pw)
    
    # 로그인 시도
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    print("🔓 로그인 완료")

    return driver
