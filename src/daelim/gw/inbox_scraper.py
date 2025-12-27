# ① Standard Library
import time
from datetime import datetime

# ② Third-party Library
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def scrape_inbox(driver) -> list:

    """수신접수함에서 지정 날짜의 문서 목록 추출"""

    # 프레임으로 전환
    frame = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "right"))
    )
    driver.switch_to.frame(frame)
    #print("☑️  [진입] right 프레임")

    # 추출할 날짜 입력
    while True:
        date_str = input("📅 추출할 날짜를 입력하세요. (YYYY-MM-DD) : ")
        try:
            targetDate = datetime.strptime(date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("❌ 잘못된 형식입니다. YYYY-MM-DD 형식으로 입력해주세요.")

    DocList = []
    page = 1

    print("-" * 139)

    while True:
        # 테이블 로드 대기
        WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#DocList tbody tr"))
        )
        rows = driver.find_elements(By.CSS_SELECTOR, "#DocList tbody tr")

        # 각 행에서 데이터 추출
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")

            # 도착일자와 지정 날짜와 일치하는지 확인
            processDate = datetime.strptime(cells[8].text.strip().split()[0], "%Y-%m-%d").date()
            if processDate != targetDate:
                continue

            # 문서 정보 추출
            data1 = row.get_attribute("data1")
            data2 = row.get_attribute("data2")
            data7 = row.get_attribute("data7")

            # 회송된 문서는 제외
            if data2 == "2":
                continue

            url = f"https://gw.daelim.ac.kr/ezApprovalG/recevGSusin.do?docID={data1}&draftFlag=SUSIN&uOrgID={data7}"
            img = f"https://gw.daelim.ac.kr/fileroot/0/files/upload_common/{datetime.today().strftime('%Y%m%d')}/{data1}.png"
            docTitle = cells[1].text.strip()
            writerName = cells[4].text.strip()
            sentDeptName = cells[5].text.strip()

            # 추출된 정보 출력
            print(f"- 도착일자\t : {str(processDate)}\n- URL\t\t : {url}\n- 이미지\t : {img}\n- 협조전 제목\t : {docTitle}\n- 발신부서\t : {sentDeptName}\n- 기안자\t : {writerName}")
            print("-" * 139)

            DocList.append([str(processDate), url, img, docTitle, sentDeptName, writerName])

        # 마지막 문서 도착일자 확인
        lastArrival = rows[-1].find_elements(By.TAG_NAME, "td")[8].text.strip()
        lastDate = datetime.strptime(lastArrival.split()[0], "%Y-%m-%d").date()

        # 페이지의 마지막 문서 도착일자가 지정 날짜이거나 이후일 때
        if lastDate >= targetDate:
            page += 1
            try:
                # 다음 페이지로 이동
                next_page = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, f"//span[@onclick='goToPageByNum({page})']"))
                )
                next_page.click()
                time.sleep(1) # 페이지 로딩시간
                continue
            except:
                print("⚠️ 다음 페이지 없음 또는 클릭 실패")
                break
        else:
            break

    return DocList
