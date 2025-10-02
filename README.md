# 개요
대림대학교 그룹웨어의 수신접수함에서 협조전 문서를 자동으로 수집하여 `Google Sheets`와 `Notion DB`에 연동하는 **업무 리스트업** 프로그램입니다.

<br>

## 📋 목차

- [주요 기능](#-주요-기능-)
- [사용 기술 및 언어](#-사용-기술-및-언어-)
- [프로젝트 구조](#-프로젝트-구조-)
- [설치 방법](#-설치-방법-)
- [환경 설정](#-환경-설정-)
- [사용 방법](#-사용-방법-)
- [동작 흐름](#-동작-흐름-)
- [문제 해결](#-문제-해결-)
- [주의 사항](#-주의사항-)

<br>

---

<br>

## [ 주요 기능 ]
| **기능** | **설명** |
-|-
**자동 로그인** | 대림대학교 학생포털에 자동으로 로그인합니다.
**협조전 스크래핑** | 지정한 날짜의 협조전 문서를 자동으로 수집합니다.
**다중 페이지 처리** | 여러 페이지에 걸쳐 있는 문서를 자동으로 탐색합니다.
**Google Sheets 연동** | 수집된 데이터를 Google Sheets에 자동으로 추가합니다.
**Notion DB 연동** | 수집된 데이터를 Notion 데이터베이스에 자동으로 추가합니다.

<br>

## [ 사용 기술 및 언어 ]
- **Python 3.x**
- **Selenium**
- **Google Sheets API**
- **Notion API**
- **python-dotenv**

<br>

## [ 프로젝트 구조 ]
```
.
│  .env.example                     # 환경변수 예시 파일
│  main.py                          # 프로그램 진입점
│  README.md                        # 프로젝트 문서
│  requirements.txt                 # Python 패키지 의존성
│
├─credentials                       # Google API 인증 정보
│      credentials.json
│
├─drivers                           # ChromeDriver 실행 파일
│      chromedriver.exe
│
└─src
    │  app.py                       # 메인 애플리케이션 로직
    │  config.py                    # 환경 설정 관리
    │
    ├─daelim
    │  ├─gw
    │  │      inbox_scraper.py      # 수신접수함 스크래핑
    │  │
    │  └─pt
    │          login_flow.py        # 로그인 처리
    │          menu_navigation.py   # 수신접수합으로 이동
    │
    └─infra
        ├─browser
        │      chrome_driver.py     # Chrome WebDriver 설정
        │
        └─service
                notion.py           # Notion API 연동
                spreadsheet.py      # Google Sheets API 연동
```

## [ 설치 방법 ]
### 1️⃣ Python 패키지 설치
```bash
pip install -r requirements.txt
```
**requirements.txt 내용:**
```
selenium
python-dotenv
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
requests
```

### 2️⃣ ChromeDriver 설치
1. Chrome 브라우저 버전 확인: `chrome://settings/help`
2. [ChromeDriver 다운로드](https://chromedriver.chromium.org/downloads)
3. `drivers/chromedriver.exe` 경로에 저장

<br>

## [ 환경 설정 ]
### 1️⃣ 환경변수 파일 생성
`.env.example`을 복사하여 `.env` 파일을 생성합니다.
```bash
cp .env.example .env
```

### 2️⃣ .env 파일 작성
```env
# DUC (대림대학교 학생포털 로그인 정보)
URL=https://pt.daelim.ac.kr
USER_ID=your_student_id
USER_PW=your_password

# Selenium (ChromeDriver 경로)
CHROME_DRIVER_PATH=drivers/chromedriver.exe

# Google Sheets API
SPREADSHEET_ID=your_spreadsheet_id
CREDENTIALS_PATH=credentials/credentials.json

# Notion API
NOTION_TOKEN=your_notion_integration_token
DB_ID=your_notion_database_id
```

### 3️⃣ Google Sheets API 설정
1. [Google Cloud Console](https://console.cloud.google.com/)에서 프로젝트 생성
2. Google Sheets API 활성화
3. 서비스 계정 생성 및 JSON 키 다운로드
4. `credentials/credentials.json`에 저장
5. 서비스 계정 이메일을 Google Sheets에 공유 권한 부여
**Google Sheets 형식:**
- 시트 이름: `AI시스템과`
- 컬럼 구성: `도착일자 | URL | 이미지 | 협조전 제목 | 발신부서 | 기안자`

### 4️⃣ Notion API 설정
1. [Notion Developers](https://www.notion.so/my-integrations)에서 Integration 생성
2. Internal Integration Token 복사
3. Notion 데이터베이스 생성 후 Integration 연결
4. 데이터베이스 ID 확인 (URL에서 추출)

**Notion DB 속성 구성:**
속성명 | 유형
-|-
**도착일자** | Date 타입
**URL** | URL 타입
**이미지** | URL 타입
**협조전 제목** | Title 타입
**발신부서** | Text 타입
**기안자** | Text 타입

<br>

## [ 사용 방법 ]
### 프로그램 실행
```bash
python main.py
```

### 실행 과정
1. 브라우저가 자동으로 열립니다.
2. 대림대학교 포털에 자동 로그인됩니다.
3. 그룹웨어 수신접수함으로 이동합니다.
4. **날짜 입력 프롬프트**가 나타나면 원하는 날짜를 입력합니다.
   ```
   📅 추출할 날짜를 입력하세요. (YYYY-MM-DD) : 2025-09-26
   ```
5. 해당 날짜의 협조전 문서가 자동으로 수집됩니다.
6. `Google Sheets`와 `Notion DB`에 데이터가 추가됩니다.
7. 작업 완료 후 Enter 키를 누르면 브라우저가 종료됩니다.

### 실행 예시
```
💻 브라우저가 열렸습니다.
☑️ [진입] PortalMain 프레임
🔓 로그인 완료
☑️ [진입] right 프레임
📅 추출할 날짜를 입력하세요. (YYYY-MM-DD) : 2025-09-26
---------------------------------------------------------------------------
- 도착일자      : 2025-09-26
- URL		   : https://gw.daelim.ac.kr/ezApprovalG/recevGSusin.do?docID=...
- 이미지        : https://gw.daelim.ac.kr/fileroot/0/files/upload_common/...
- 협조전 제목    : 2025학년도 2학기 중간고사 시행 안내
- 발신부서      : 교육행정팀
- 기안자        : 김대림
---------------------------------------------------------------------------
✅ 1행 추가 완료 : Google Sheets
✅ 1행 추가 완료 : Notion DB
🔍 작업 완료! Enter 키를 누르면 브라우저가 종료됩니다...
```

<br>

## [ 동작 흐름 ]
```
1. 프로그램 진입점 (main.py)
   ↓
2. 메인 로직 실행 (app.py - main())
   │
   ├─ [설정 단계]
   │  ├─ 환경 설정 로드 (config.py - load_settings())
   │  └─ Chrome WebDriver 생성 (chrome_driver.py - build_driver())
   │
   ├─ [로그인 및 이동]
   │  ├─ 포털 로그인 (login_flow.py - login_to_portal())
   │  │  - 포털 접속
   │  │  - PortalMain 프레임 진입
   │  │  - 로그인 정보 입력 및 로그인
   │  │
   │  └─ 수신접수함 이동 (menu_navigation.py - go_to_inbox())
   │     - 수신접수 아이콘 클릭
   │     - 새 창으로 전환
   │
   ├─ [데이터 수집]
   │  └─ 협조전 스크래핑 (inbox_scraper.py - scrape_inbox())
   │     - right 프레임 진입
   │     - 사용자 입력: 추출 날짜 (YYYY-MM-DD)
   │     - 페이지 순회하며 데이터 수집
   │     - DocList 반환
   │
   ├─ [데이터 연동]
   │  ├─ Google Sheets 추가 (spreadsheet.py - append_to_spreadsheet())
   │  │  - 서비스 계정 인증
   │  │  - Sheets API로 데이터 추가
   │  │
   │  └─ Notion DB 추가 (notion.py - append_to_notion())
   │     - Notion API 인증
   │     - 각 문서를 Notion 페이지로 생성
   │
   └─ [종료]
      - 사용자 입력 대기 (Enter)
      - 브라우저 종료 (driver.quit())
```
<br>

## [ 문제 해결 ]
### 1️⃣ 로그인이 안 될 때
- `.env` 파일의 `USER_ID`와 `USER_PW`를 확인하세요.
- 포털 사이트에서 직접 로그인이 되는지 확인하세요.

### 2️⃣ ChromeDriver 오류
```
SessionNotCreatedException: session not created: This version of ChromeDriver only supports Chrome version XX
```
**해결 방법:**
1. Chrome 브라우저 버전 확인: `chrome://settings/help`
2. 동일한 버전의 ChromeDriver 다운로드
3. `drivers/chromedriver.exe` 교체

### 3️⃣ Google Sheets 연동 실패
- `credentials.json` 파일이 올바른 경로에 있는지 확인
- 서비스 계정 이메일에 Google Sheets 편집 권한이 있는지 확인
- `SPREADSHEET_ID`가 정확한지 확인

### 4️⃣ Notion 연동 실패
- `NOTION_TOKEN`이 올바른지 확인
- Integration이 데이터베이스에 연결되어 있는지 확인
- 데이터베이스 속성 이름이 정확히 일치하는지 확인

### 5️⃣ 날짜 입력 오류
```
❌ 잘못된 형식입니다. YYYY-MM-DD 형식으로 입력
```
**해결 방법:**
- 날짜를 `2025-09-26` 형식으로 입력
- 하이픈(`-`)을 반드시 포함

<br>

## [ 주의사항 ]
- 본 프로그램은 **개인 학습 및 업무 리스트업 목적**으로 제작되었습니다.
- **학교 계정 정보**는 절대 공유하지 마십시오.
- `.env` 파일과 `credentials.json` 파일은 Git에 커밋하지 마십시오.
- 과도한 요청은 서버에 부담을 줄 수 있으니 적절히 사용하십시오.

<br>

---

<br>

**💡 Tip**: 문제가 발생하면 먼저 각 설정값이 올바른지 확인하고, 브라우저를 수동으로 조작하여 정상 동작하는지 테스트하십시오.
