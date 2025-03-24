import requests
from bs4 import BeautifulSoup

# 네이버 TV 피드 페이지 URL
url = "https://tv.naver.com/feed"

# User-Agent 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 웹 페이지 요청
response = requests.get(url, headers=headers)
html = response.text

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(html, "html.parser")

# 급상승 영상 리스트 찾기
videos = soup.select("div.cds")  # 급상승 영상이 포함된 div 클래스

print("📈 네이버 TV 급상승 영상 📈")
for idx, video in enumerate(videos, start=1):
    title_tag = video.select_one("dt.title a")  # 제목 찾기
    if title_tag:
        title = title_tag.text.strip()
        link = "https://tv.naver.com" + title_tag["href"]  # URL 연결
        print(f"{idx}. {title} - {link}")