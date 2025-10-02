# ① Standard Library
import requests

# ③ Local Modules
from src.config import Settings

def append_to_notion(settings: Settings, DocList: list) -> None:

    """노션DB에 연동"""

    # 헤더 설정
    headers = {
        "Authorization": f"Bearer {settings.notion_token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    cnt = 0

    # 각 문서를 Notion 페이지로 생성
    for row in DocList:
        # 속성 : 도착일자 | URL | 이미지 | 협조전 제목 | 발신부서 | 기안자
        processDate, url, img, docTitle, sentDeptName, writerName = row

        # DB 속성에 맞는 페이지 생성
        payload = {
            "parent": {"database_id": settings.db_id},
            "properties": {
                "도착일자": {"date": {"start": processDate}},
                "URL": {"url": url},
                "이미지": {"url": img},
                "협조전 제목": {"title": [{"text": {"content": docTitle}}]},
                "발신부서": {"rich_text": [{"text": {"content": sentDeptName}}]},
                "기안자": {"rich_text": [{"text": {"content": writerName}}]},
            },
        }

        # 페이지 생성 요청
        response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=payload)

        if response.status_code != 200:
            print(f"❌ 추가 실패 : Notion DB")
            break

        cnt += 1

    # for문이 break문 없이 완료된 경우에만 실행
    else:
        print(f"✅ {cnt}행 추가 완료 : Notion DB")

    return None
